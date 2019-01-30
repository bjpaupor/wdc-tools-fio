#ifndef FIO_SPRAND_H
#define FIO_SPRAND_H

#include <inttypes.h>

#include <lib/lfsr.h>

struct fio_file;
struct thread_data;

/*
 * blocknum			erase block number
 * cur_block_pages		page number within block
 * border			page number for transition to invalidate
 * pagelist			written pages within the block
 * pagesperblock
 * cur_state_blocks		how many pages for given state have been issued
 * blocks_per_state
 *
 */

struct sprand_state {
	uint64_t blockcount;
	uint64_t blocknum;
	uint64_t cur_block_pages;
	uint64_t limit;
	uint64_t *pagelist;
	uint64_t pagesperblock;
	uint64_t cur_state_blocks;
	uint64_t blocks_per_state;
	uint64_t seq_offset;
	uint64_t validpages;
	double remainder;
	double n_bar;
	struct fio_lfsr lfsr;
};

int sprand_next(struct thread_data *td, struct fio_file *f, uint64_t *b);
int sprand_init(struct thread_data *td);
void sprand_free(struct thread_data *td, struct fio_file *f);

#endif
