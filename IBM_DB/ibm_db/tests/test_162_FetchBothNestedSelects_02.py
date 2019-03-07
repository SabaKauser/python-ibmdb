#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

from __future__ import print_function
import sys
import unittest
import ibm_db
import config
from testfunctions import IbmDbTestFunctions

class IbmDbTestCase(unittest.TestCase):

    def test_162_FetchBothNestedSelects_02(self):
        obj = IbmDbTestFunctions()
        obj.assert_expect(self.run_test_162)

    def run_test_162(self):
        conn = ibm_db.connect(config.database, config.user, config.password)

        server = ibm_db.server_info( conn )
        if (server.DBMS_NAME[0:3] == 'IDS'):
            op = {ibm_db.ATTR_CASE: ibm_db.CASE_UPPER}
            ibm_db.set_option(conn, op, 1)

        result = ibm_db.exec_immediate(conn, "select * from emp_act order by projno")
        row = ibm_db.fetch_both(result)
        # will only retrieve 10 records
        count = 1
        while ( row ):
            print("Record ",count,": %6s  %-6s %3d %9s %10s %10s %6s " % (row[0], row[1], row[2], row['EMPTIME'], row['EMSTDATE'], row['EMENDATE'], row[0]))

            result2 = ibm_db.exec_immediate(conn,"select * from employee where employee.empno='" + row['EMPNO'] + "'")
            row2 = ibm_db.fetch_both(result2)
            if row2:        
                print(">>%s,%s,%s,%s,%s,%s,%s" % (row2['EMPNO'], row2['FIRSTNME'],row2['MIDINIT'], row2[3], row2[3], row2[5], row2[6]))      
            count = count + 1
            if (count > 10):
                break
            row = ibm_db.fetch_both(result)
#__END__
#__LUW_EXPECTED__
#Record  1 : 000010  AD3100  10      0.50 1982-01-01 1982-07-01 000010 
#>>000010,CHRISTINE,I,HAAS,HAAS,3978,1965-01-01
#Record  2 : 000070  AD3110  10      1.00 1982-01-01 1983-02-01 000070 
#>>000070,EVA,D,PULASKI,PULASKI,7831,1980-09-30
#Record  3 : 000230  AD3111  60      1.00 1982-01-01 1982-03-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  4 : 000230  AD3111  60      0.50 1982-03-15 1982-04-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  5 : 000230  AD3111  70      0.50 1982-03-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  6 : 000230  AD3111  80      0.50 1982-04-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  7 : 000230  AD3111 180      1.00 1982-10-15 1983-01-01 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  8 : 000240  AD3111  70      1.00 1982-02-15 1982-09-15 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  9 : 000240  AD3111  80      1.00 1982-09-15 1983-01-01 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  10 : 000250  AD3112  60      1.00 1982-01-01 1982-02-01 000250 
#>>000250,DANIEL,S,SMITH,SMITH,0961,1969-10-30
#__ZOS_EXPECTED__
#Record  1 : 000010  AD3100  10      0.50 1982-01-01 1982-07-01 000010 
#>>000010,CHRISTINE,I,HAAS,HAAS,3978,1965-01-01
#Record  2 : 000070  AD3110  10      1.00 1982-01-01 1983-02-01 000070 
#>>000070,EVA,D,PULASKI,PULASKI,7831,1980-09-30
#Record  3 : 000240  AD3111  80      1.00 1982-09-15 1983-01-01 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  4 : 000240  AD3111  70      1.00 1982-02-15 1982-09-15 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  5 : 000230  AD3111 180      1.00 1982-10-15 1983-01-01 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  6 : 000230  AD3111  80      0.50 1982-04-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  7 : 000230  AD3111  70      0.50 1982-03-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  8 : 000230  AD3111  60      0.50 1982-03-15 1982-04-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  9 : 000230  AD3111  60      1.00 1982-01-01 1982-03-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  10 : 000250  AD3112  60      1.00 1982-01-01 1982-02-01 000250 
#>>000250,DANIEL,S,SMITH,SMITH,0961,1969-10-30
#__SYSTEMI_EXPECTED__
#Record  1 : 000010  AD3100  10      0.50 1982-01-01 1982-07-01 000010 
#>>000010,CHRISTINE,I,HAAS,HAAS,3978,1965-01-01
#Record  2 : 000070  AD3110  10      1.00 1982-01-01 1983-02-01 000070 
#>>000070,EVA,D,PULASKI,PULASKI,7831,1980-09-30
#Record  3 : 000230  AD3111  60      1.00 1982-01-01 1982-03-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  4 : 000230  AD3111  60      0.50 1982-03-15 1982-04-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  5 : 000230  AD3111  70      0.50 1982-03-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  6 : 000230  AD3111  80      0.50 1982-04-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  7 : 000230  AD3111 180      1.00 1982-10-15 1983-01-01 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  8 : 000240  AD3111  70      1.00 1982-02-15 1982-09-15 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  9 : 000240  AD3111  80      1.00 1982-09-15 1983-01-01 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  10 : 000250  AD3112  60      1.00 1982-01-01 1982-02-01 000250 
#>>000250,DANIEL,S,SMITH,SMITH,0961,1969-10-30
#__IDS_EXPECTED__
#Record  1 : 000010  AD3100  10      0.50 1982-01-01 1982-07-01 000010 
#>>000010,CHRISTINE,I,HAAS,HAAS,3978,1965-01-01
#Record  2 : 000070  AD3110  10      1.00 1982-01-01 1983-02-01 000070 
#>>000070,EVA,D,PULASKI,PULASKI,7831,1980-09-30
#Record  3 : 000240  AD3111  80      1.00 1982-09-15 1983-01-01 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  4 : 000230  AD3111 180      1.00 1982-10-15 1983-01-01 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  5 : 000230  AD3111  80      0.50 1982-04-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  6 : 000240  AD3111  70      1.00 1982-02-15 1982-09-15 000240 
#>>000240,SALVATORE,M,MARINO,MARINO,3780,1979-12-05
#Record  7 : 000230  AD3111  70      0.50 1982-03-15 1982-10-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  8 : 000230  AD3111  60      0.50 1982-03-15 1982-04-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  9 : 000230  AD3111  60      1.00 1982-01-01 1982-03-15 000230 
#>>000230,JAMES,J,JEFFERSON,JEFFERSON,2094,1966-11-21
#Record  10 : 000250  AD3112  80      0.25 1982-08-15 1982-10-15 000250 
#>>000250,DANIEL,S,SMITH,SMITH,0961,1969-10-30
