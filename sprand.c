#include <math.h>

#include "file.h"
#include "fio.h"
#include "sprand.h"
#include "lib/lambertsw.h"

static void sprand_update_limit(struct sprand_state *sp)
{
	sp->cur_state_blocks++;
	if (sp->cur_state_blocks == sp->blocks_per_state) {
		sp->cur_state_blocks = 0;
		sp->blocks_per_state = 0;

		while (sp->blocks_per_state == 0) {
			sp->limit++;

			/*
			 * Rearrange Dedrick eq 3 to obtain an expression
			 * for the fraction of all blocks with given number of
			 * valid pages and multiply by total number of blocks.
			 * This produces the number of blocks with the given
			 * number of valid pages.
			 */
			sp->blocks_per_state = floor(sp->n_bar * sp->blockcount / sp->limit + sp->remainder);

			/*
			 * we are rounding to obtain an integer above
			 * so save the remainder for use next time
			 */
			sp->remainder = (sp->n_bar * sp->blockcount / sp->limit + sp->remainder) - sp->blocks_per_state;
			dprint(FD_RANDOM, "sprand: valid_pages = %lu, blocks_per_state = %lu, remainder = %10.7f\n",
					sp->limit, sp->blocks_per_state, sp->remainder);
		}
	}
}

int sprand_next(struct thread_data *td, struct fio_file *f, uint64_t *b)
{
	struct sprand_state *sp = &f->sprand;

	/* move on to the next block */
	if (sp->cur_block_pages == sp->pagesperblock) {
		sp->blocknum++;
		sp->cur_block_pages = 0;

		sprand_update_limit(sp);

		dprint(FD_RANDOM, "sprand: block %lu, limit = %lu\n",
				sp->blocknum, sp->limit);
	}

	if (sp->cur_block_pages < sp->limit) {
		uint64_t off = 0;

		/* get offset from lfsr */
		assert(fio_file_lfsr(f));
		if (lfsr_next(&f->lfsr, &off))
			assert(0);	// TODO figure out what to do here

		*b = off;
		sp->pagelist[sp->cur_block_pages] = off;
	} else if (sp->cur_block_pages < sp->pagesperblock) {
		/* invalidate already written page */
		*b = sp->pagelist[rand_between(&td->sprand_state, 0, sp->limit-1)];
	} else
		assert(0);

	dprint(FD_RANDOM, "sprand: block %llu, cur_block_pages %llu, "
			"cur_state_blocks %llu, blocks_per_state %llu, "
			"offset %llu, invalidate %d\n",
			(unsigned long long) sp->blocknum,
			(unsigned long long) sp->cur_block_pages,
			(unsigned long long) sp->cur_state_blocks,
			(unsigned long long) sp->blocks_per_state,
			(unsigned long long) *b,
			sp->cur_block_pages >= sp->limit);

	sp->cur_block_pages++;
	return 0;
}

int sprand_init(struct thread_data *td)
{
	struct fio_file *f;
	struct thread_options *o = &td->o;
	struct sprand_state *sp;
	unsigned int i;
	double op, wa;

	for_each_file(td, f, i) {
		sp = &f->sprand;
		sp->blocknum = sp->cur_block_pages = sp->cur_state_blocks = 0;
		sp->remainder = 0.0;
		sp->pagesperblock = o->spphyscapacity / o->bs[DDIR_WRITE] / o->spebcount;
		sp->blockcount = o->spebcount;

		sp->pagelist = malloc(sp->pagesperblock * sizeof(uint64_t));
		if (!sp->pagelist)
			return 1;

		op = (double) (o->spphyscapacity - o->splogcapacity) / o->splogcapacity;

		/*
		 * write amplification
		 * Xiang and Kurkoski 2011 eq 12
		 */
		wa = (-1.0 - op) /
			(-1.0 - op - lambertsw((-1.0 - op) * exp(-1.0 - op)));

		/*
		 * n_gc is the number of valid pages in the erase block
		 * chosen for grooming
		 *
		 * n_bar is the average fraction of valid pages
		 * contained in blocks with more than n_gc valid pages
		 * Dedrick eq 4b
		 * Dedrick references are to OLD v1.3 which is not in
		 * the python bitbucket repository
		 */
		sp->n_bar = wa / (op + 1.0);

		/*
		 * n_gc formula is from Dedrick eq 6
		 * sp->limit = n_gc for the first block
		 * Start writing blocks so that the one with the least
		 * valid data has n_gc valid pages
		 * Dedrick is imprecise regarding how many blocks have
		 * n_gc valid pages but there must be at least one
		 */
		sp->limit = sp->pagesperblock * (wa - 1.0) / wa;

		/* write one block with n_gc valid pages */
		sp->blocks_per_state = 1;

		dprint(FD_RANDOM, "sprand: op = %10.7f, wa = %10.7f, n_bar = %10.7f\n",
				op, wa, sp->n_bar);
		dprint(FD_RANDOM, "sprand: pagesperblock = %llu, blocks per state = %llu\n",
				(unsigned long long) sp->pagesperblock,
				(unsigned long long) sp->blocks_per_state);
		dprint(FD_RANDOM, "sprand: block %lu, limit = %lu\n",
				sp->blocknum, sp->limit);
	}

	return 0;
}

void sprand_free(struct thread_data *td, struct fio_file *f)
{
	struct thread_options *o = &td->o;
	struct sprand_state *sp = &f->sprand;

	if (o->random_distribution != FIO_RAND_DIST_SPRAND)
		return;

	free(sp->pagelist);
}
