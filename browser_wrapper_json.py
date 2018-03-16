import json

# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
# Define data
operator = {}
circle = {}
file_p = ""

circle.update({"bihar":{"300":{"on-net":20000,
                               "off-net":40000,
                               "local":20000,
                               "std":1000
                              }
                       }
              }
             )
operator.update({"airtel":circle})

for each,val in operator.items():
        for circle,data in val.items():
                # Write JSON file
                file_p = each+"_"+circle+".json"
                with open(file_p, 'w') as outfile:
                         str_ = json.dumps(data,
                                 indent=4, sort_keys=True,
                                 separators=(',', ': '), ensure_ascii=False)
                         outfile.write(to_unicode(str_))

