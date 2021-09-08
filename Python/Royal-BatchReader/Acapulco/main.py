import Flist
import FEread
import encoder
import Dread
import time

start_time = time.time()
print("\033[93mData gathering..")
Flist.run()
flist_time = time.time()
print("\033[93mData parsing..")
Dread.run()
dread_time = time.time()
print("\033[93mFront-end data extraction..")
FEread.run()
feread_time = time.time()
print("\033[93mData comparison and report generation..")
encoder.run()
encoder_time = time.time()
end_time = time.time()
print("\n\n\033[96m--- Validation complete... Time:          | %s seconds.---" % (round(end_time - start_time, 5)))
print("\033[92m--- File listing time:                    | %s seconds.---" % (round(flist_time - start_time, 5)))
print("\033[92m--- Data read and parsing time:           | %s seconds.---" % (round(dread_time - flist_time, 5)))
print("\033[92m--- Front-end data recovery time:         | %s seconds.---" % (round(feread_time - dread_time, 5)))
print("\033[92m--- Data validation and report execution: | %s seconds.---" % (round(encoder_time - feread_time, 5)))
