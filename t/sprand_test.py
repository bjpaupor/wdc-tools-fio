#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only
#
# Copyright (c) 2020 Western Digital Corporation or its affiliates.
#
"""
# sprand_test.py
#
# Carry out a very basic test for sprand.
#
# This runs only the "Example 3: toy example" from
# https://esswiki.wdc.com/display/~vfu/sprandomize%3A+single-pass+randomization
#
# This checks only the following:
#   1) values calculated in the first 3 lines of debug output
#   2) per-block values calculated for 32 IOs; these values depend crucially on fio's
#       random number generation routines and seeds. So any changes thereto will
#       lead to test failures
#
#
#
#
./fio/fio --debug=random --name=test --ioengine=null --random_distribution=sprandom:10GM:9062M:1000 --bs=4k --size=9062M --io_size=128k --random_generator=lfsr --rw=randwrite
fio: set debug option random
test: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=null, iodepth=1
fio-3.12-123-g61c87
Starting 1 process
random   8617  sprand: op =  0.1299934, wa =  4.5269799, n_bar =  4.0062004
random   8617  sprand: pagesperblock = 2621, blocks per state = 1
random   8617  sprand: block 0, limit = 2042, avglimit = 2042
random   8617  sprand: block 0, cur_block_pages 0, cur_state_blocks 0, blocks_per_state 1, offset 157435, invalidate 0, sp-lfsr 0
random   8617  sprand: block 0, cur_block_pages 1, cur_state_blocks 0, blocks_per_state 1, offset 2175869, invalidate 0, sp-lfsr 1746
random   8617  sprand: block 0, cur_block_pages 2, cur_state_blocks 0, blocks_per_state 1, offset 543967, invalidate 0, sp-lfsr 832
random   8617  sprand: block 0, cur_block_pages 3, cur_state_blocks 0, blocks_per_state 1, offset 991539, invalidate 0, sp-lfsr 393
random   8617  sprand: block 0, cur_block_pages 4, cur_state_blocks 0, blocks_per_state 1, offset 157435, invalidate 1, sp-lfsr 2244
random   8617  sprand: block 0, cur_block_pages 5, cur_state_blocks 0, blocks_per_state 1, offset 648230, invalidate 0, sp-lfsr 1099
random   8617  sprand: block 0, cur_block_pages 6, cur_state_blocks 0, blocks_per_state 1, offset 991539, invalidate 1, sp-lfsr 2597
random   8617  sprand: block 0, cur_block_pages 7, cur_state_blocks 0, blocks_per_state 1, offset 1372691, invalidate 0, sp-lfsr 1696
random   8617  sprand: block 0, cur_block_pages 8, cur_state_blocks 0, blocks_per_state 1, offset 695874, invalidate 0, sp-lfsr 889
random   8617  sprand: block 0, cur_block_pages 9, cur_state_blocks 0, blocks_per_state 1, offset 2175869, invalidate 1, sp-lfsr 2492
random   8617  sprand: block 0, cur_block_pages 10, cur_state_blocks 0, blocks_per_state 1, offset 1396513, invalidate 0, sp-lfsr 1271
random   8617  sprand: block 0, cur_block_pages 11, cur_state_blocks 0, blocks_per_state 1, offset 349128, invalidate 0, sp-lfsr 1894
random   8617  sprand: block 0, cur_block_pages 12, cur_state_blocks 0, blocks_per_state 1, offset 1223140, invalidate 0, sp-lfsr 922
random   8617  sprand: block 0, cur_block_pages 13, cur_state_blocks 0, blocks_per_state 1, offset 1660146, invalidate 0, sp-lfsr 484
random   8617  sprand: block 0, cur_block_pages 14, cur_state_blocks 0, blocks_per_state 1, offset 1878649, invalidate 0, sp-lfsr 219
random   8617  sprand: block 0, cur_block_pages 15, cur_state_blocks 0, blocks_per_state 1, offset 157435, invalidate 1, sp-lfsr 2157
random   8617  sprand: block 0, cur_block_pages 16, cur_state_blocks 0, blocks_per_state 1, offset 469662, invalidate 0, sp-lfsr 1586
random   8617  sprand: block 0, cur_block_pages 17, cur_state_blocks 0, blocks_per_state 1, offset 1283407, invalidate 0, sp-lfsr 816
random   8617  sprand: block 0, cur_block_pages 18, cur_state_blocks 0, blocks_per_state 1, offset 957610, invalidate 0, sp-lfsr 433
random   8617  sprand: block 0, cur_block_pages 19, cur_state_blocks 0, blocks_per_state 1, offset 1660146, invalidate 1, sp-lfsr 2264
random   8617  sprand: block 0, cur_block_pages 20, cur_state_blocks 0, blocks_per_state 1, offset 1527381, invalidate 0, sp-lfsr 1093
random   8617  sprand: block 0, cur_block_pages 21, cur_state_blocks 0, blocks_per_state 1, offset 1372691, invalidate 1, sp-lfsr 2594
random   8617  sprand: block 0, cur_block_pages 22, cur_state_blocks 0, blocks_per_state 1, offset 381845, invalidate 0, sp-lfsr 1336
random   8617  sprand: block 0, cur_block_pages 23, cur_state_blocks 0, blocks_per_state 1, offset 2288074, invalidate 0, sp-lfsr 693
random   8617  sprand: block 0, cur_block_pages 24, cur_state_blocks 0, blocks_per_state 1, offset 1878649, invalidate 1, sp-lfsr 2394
random   8617  sprand: block 0, cur_block_pages 25, cur_state_blocks 0, blocks_per_state 1, offset 95461, invalidate 0, sp-lfsr 1156
random   8617  sprand: block 0, cur_block_pages 26, cur_state_blocks 0, blocks_per_state 1, offset 2144882, invalidate 0, sp-lfsr 619
random   8617  sprand: block 0, cur_block_pages 27, cur_state_blocks 0, blocks_per_state 1, offset 1223140, invalidate 1, sp-lfsr 2357
random   8617  sprand: block 0, cur_block_pages 28, cur_state_blocks 0, blocks_per_state 1, offset 23865, invalidate 0, sp-lfsr 1636
random   8617  sprand: block 0, cur_block_pages 29, cur_state_blocks 0, blocks_per_state 1, offset 2109084, invalidate 0, sp-lfsr 795
random   8617  sprand: block 0, cur_block_pages 30, cur_state_blocks 0, blocks_per_state 1, offset 469662, invalidate 1, sp-lfsr 2445
random   8617  sprand: block 0, cur_block_pages 31, cur_state_blocks 0, blocks_per_state 1, offset 5966, invalidate 0, sp-lfsr 1610#
#
#
# USAGE
# python3 sprand_test.py [-f fio-path] [-a artifact-root] [--debug]
#
#
"""

import os
import sys
import time
import argparse
import subprocess
from pathlib import Path


class FioLatTest():
    """fio latency percentile test."""

    def __init__(self, artifact_root, test_options, debug):
        """
        artifact_root   root directory for artifacts (subdirectory will be created under here)
        test            test specification
        """
        self.artifact_root = artifact_root
        self.test_options = test_options
        self.debug = debug
        self.filename = None
        self.json_data = None
        self.terse_data = None

        self.test_dir = os.path.join(self.artifact_root,
                                     "{:03d}".format(self.test_options['test_id']))
        if not os.path.exists(self.test_dir):
            os.mkdir(self.test_dir)

        self.filename = "sprand_test{:03d}".format(self.test_options['test_id'])

    def run_fio(self, fio_path):
        """Run a test."""

        fio_args = [
            "--name=sprand_test",
            "--ioengine={ioengine}".format(**self.test_options),
            "--random_distribution={random_distribution}".format(**self.test_options),
            "--bs={bs}".format(**self.test_options),
            "--size={size}".format(**self.test_options),
            "--io_size={io_size}".format(**self.test_options),
            "--random_generator={random_generator}".format(**self.test_options),
            "--rw={rw}".format(**self.test_options),
        ]
        for opt in ['debug', 'output', ]:
            if opt in self.test_options:
                option = '--{0}={{{0}}}'.format(opt)
                fio_args.append(option.format(**self.test_options))

        command = [fio_path] + fio_args
        with open(os.path.join(self.test_dir, "{0}.command".format(self.filename)), "w+") as \
                command_file:
            command_file.write("%s\n" % command)

        passed = True
        stdout_file = open(os.path.join(self.test_dir, "{0}.stdout".format(self.filename)), "w+")
        stderr_file = open(os.path.join(self.test_dir, "{0}.stderr".format(self.filename)), "w+")
        exitcode_file = open(os.path.join(self.test_dir,
                                          "{0}.exitcode".format(self.filename)), "w+")
        try:
            proc = None
            # Avoid using subprocess.run() here because when a timeout occurs,
            # fio will be stopped with SIGKILL. This does not give fio a
            # chance to clean up and means that child processes may continue
            # running and submitting IO.
            proc = subprocess.Popen(command,
                                    stdout=stdout_file,
                                    stderr=stderr_file,
                                    cwd=self.test_dir,
                                    universal_newlines=True)
            proc.communicate(timeout=300)
            exitcode_file.write('{0}\n'.format(proc.returncode))
            passed &= (proc.returncode == 0)
        except subprocess.TimeoutExpired:
            proc.terminate()
            proc.communicate()
            assert proc.poll()
            print("Timeout expired")
            passed = False
        except Exception:
            if proc:
                if not proc.poll():
                    proc.terminate()
                    proc.communicate()
            print("Exception: %s" % sys.exc_info())
            passed = False
        finally:
            stdout_file.close()
            stderr_file.close()
            exitcode_file.close()

        return passed


class Test001(FioLatTest):
    """Test object for Test 1."""

    def check(self):
        """Check Test 1 output."""

        filename = os.path.join(self.test_dir, "{0}.stdout".format(self.filename))
        with open(filename, 'r') as file:
            file_data = file.read()

        op = False
        pagesperblock = False
        block = False
        blocknum = 0
        cur_block_pages = 0
        cur_state_blocks = 0
        blocks_per_state = 1
        offset = [157435, 2175869, 543967, 991539, -1, 648230, -1, 1372691, 695874,
                  -1, 1396513, 349128, 1223140, 1660146, 1878649, -1,
                  469662, 1283407, 957610, -1, 1527381, -1, 381845, 2288074,
                  -1, 95461, 2144882, 1223140, 23865, 2109084, -1, 5966]
        invalidate = [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1,
                      0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
        sp_lfsr = [0, 1746, 832, 393, 2244, 1099, 2597, 1696,
                   889, 2492, 1271, 1894, 922, 484, 219, 2157,
                   1586, 816, 433, 2264, 1093, 2594, 1336, 693,
                   2394, 1156, 619, 2357, 1636, 795, 2445, 1610]
        lines = file_data.split('\n')
        for line in lines:
            if not line.startswith("random "):
                continue
            line = line.replace(',', '')
            parts = line.split()
            if not op:
                assert parts[5] == '0.1299934'
                assert parts[8] == '4.5269799'
                assert parts[11] == '4.0062004'
                op = True
                continue
            if not pagesperblock:
                assert parts[5] == '2621'
                assert parts[10] == '1'
                pagesperblock = True
                continue
            if not block:
                assert parts[4] == '0'
                assert parts[7] == '2042'
                assert parts[10] == '2042'
                block = True
                continue
            assert int(parts[4]) == blocknum
            assert int(parts[6]) == cur_block_pages
            assert int(parts[8]) == cur_state_blocks
            assert int(parts[10]) == blocks_per_state
            assert int(parts[14]) == invalidate[cur_block_pages]
            assert int(parts[16]) == sp_lfsr[cur_block_pages]
            if invalidate[cur_block_pages] == 0:
                assert int(parts[12]) == offset[cur_block_pages]
            else:
                assert int(parts[12]) in offset[0:cur_block_pages]
            cur_block_pages = cur_block_pages + 1

#            print(line)

        return True


def parse_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fio', help='path to file executable (e.g., ./fio)')
    parser.add_argument('-a', '--artifact-root', help='artifact root directory')
    parser.add_argument('-d', '--debug', help='enable debug output', action='store_true')
    parser.add_argument('-s', '--skip', nargs='+', type=int,
                        help='list of test(s) to skip')
    parser.add_argument('-o', '--run-only', nargs='+', type=int,
                        help='list of test(s) to run, skipping all others')
    args = parser.parse_args()

    return args


def main():
    """Run tests of fio latency percentile reporting"""

    args = parse_args()

    artifact_root = args.artifact_root if args.artifact_root else \
        "sprand-test-{0}".format(time.strftime("%Y%m%d-%H%M%S"))
    os.mkdir(artifact_root)
    print("Artifact directory is %s" % artifact_root)

    if args.fio:
        fio = str(Path(args.fio).absolute())
    else:
        fio = 'fio'
    print("fio path is %s" % fio)

    test_list = [
        {
            # Example 3: toy example from
            # https://esswiki.wdc.com/display/~vfu/sprandomize%3A+single-pass+randomization
            "test_id": 1,
            "debug": "random",
            "ioengine": "null",
            "random_distribution": "sprandom:10G:9062M:1000",
            "bs": "4k",
            "size": "9062M",
            "io_size": "128k",
            "random_generator": "lfsr",
            "rw": "randwrite",
            "test_obj": Test001,
        },
    ]

    passed = 0
    failed = 0
    skipped = 0

    for test in test_list:
        if (args.skip and test['test_id'] in args.skip) or \
           (args.run_only and test['test_id'] not in args.run_only):
            skipped = skipped + 1
            outcome = 'SKIPPED (User request)'
        else:
            test_obj = test['test_obj'](artifact_root, test, args.debug)
            status = test_obj.run_fio(fio)
            if status:
                status = test_obj.check()
            if status:
                passed = passed + 1
                outcome = 'PASSED'
            else:
                failed = failed + 1
                outcome = 'FAILED'

        print("**********Test {0} {1}**********".format(test['test_id'], outcome))

    print("{0} tests passed, {1} failed, {2} skipped".format(passed, failed, skipped))

    sys.exit(failed)


if __name__ == '__main__':
    main()
