import requests

print("Asking server to calculate distance")
data = {
      "a": [2, 4],
      "b": [5, 6]
      }
# r = requests.post("http://127.0.0.1:5000/distance", json=data)
r = requests.post("http://vcm-9060.vm.duke.edu:5000/distance", json=data)
print("'r' = {}".format(r))
print("'r.json() = {}".format(r.json()))