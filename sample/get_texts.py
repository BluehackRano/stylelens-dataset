from __future__ import print_function
from stylelens_dataset.texts import Texts
from pprint import pprint
# create an instance of the API class
api_instance = Texts()


try:
  offset = 0
  limit = 5
  code = "5"  # == sweater


  while True:
    res = api_instance.get_texts(code, offset=offset, limit=limit)

    pprint(res)
    if limit >= len(res):
      break
    else:
      offset = offset + limit

except Exception as e:
  print("Exception when calling get_texts: %s\n" % e)
