import io
import unittest
import xmlrunner
from xmlrunner.extra.xunit_plugin import transform
from test.test_professor import testeProfessor


def new_test_suite() -> unittest.TestSuite:

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testeProfessor))
    return test_suite
if __name__ == "__main__":
    suite = new_test_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
    out = io.BytesIO()
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=out),
        failfast=False, buffer=False, catchbreak=False, exit=False
    )
    with open("unit-test.xml", "wb") as report:
        report.write(transform(out.getvalue()))