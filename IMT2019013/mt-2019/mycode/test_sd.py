import sd

def test_mysum():
  if sd.mysum(range(10)) == 45:
    print "pass"
  else:
    print "fail"

def test_average():
  if sd.average(range(10)) == 4.5:
    print "pass"
  else:
    print "fail"

def test_sqsum():
  if sd.sqsum(range(10)) == 285:
    print "pass"
  else:
    print "fail"

def test_sd():
  if sd.sd(range(10)) == 2.87228132327:
    print "pass"
  else:
    print "fail"

if __name__ == "__main__":
  test_mysum()
  test_average()
  test_sqsum()
  test_sd()
