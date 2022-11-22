[1m============================= test session starts ==============================[0m
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/ubuntu/emlov2_session08, configfile: pyproject.toml
plugins: anyio-3.6.2, hydra-core-1.2.0
collected 1 item

test_serve_cifar.py::test_cifar_inference[35.78.219.103] 35.78.219.103
response: {"cat": 0.9999998807907104, "frog": 6.343718439438817e-08, "deer": 8.761735337259324e-09, "dog": 7.807577695473356e-09, "bird": 4.8321786572103065e-09}
predicted label: cat
done testing: 10044_cat.png
_____________________________________________________
response: {"cat": 0.9991806149482727, "dog": 0.000806381634902209, "horse": 8.443865226581693e-06, "frog": 3.3593817079236032e-06, "deer": 8.411319072365586e-07}
predicted label: cat
done testing: cat.png
_____________________________________________________
response: {"ship": 0.9997318387031555, "automobile": 0.00026128790341317654, "frog": 6.3411662267753854e-06, "cat": 2.5927565161509847e-07, "horse": 1.648276537480342e-07}
predicted label: ship
done testing: ship.png
_____________________________________________________
response: {"automobile": 1.0, "ship": 8.374826873658314e-12, "airplane": 4.1300235800734164e-12, "cat": 1.4503152232772307e-14, "horse": 1.1110920804290395e-14}
predicted label: automobile
done testing: automobile.png
_____________________________________________________
response: {"dog": 1.0, "horse": 2.807739596377701e-10, "bird": 4.743920534178159e-11, "deer": 1.2096257155647105e-12, "cat": 4.942818615343014e-13}
predicted label: dog
done testing: dog.png
_____________________________________________________
response: {"airplane": 1.0, "ship": 1.7227479859327488e-11, "deer": 7.361906917413563e-11, "horse": 5.514980833121186e-11}
predicted label: airplane
done testing: airplane.png
_____________________________________________________
response: {"deer": 1.0, "bird": 3.2746629165898364e-14, "horse": 1.7689556349137318e-14, "dog": 4.118139511311795e-15, "cat": 1.3786306131928624e-15}
predicted label: deer
done testing: deer.png
_____________________________________________________
response: {"frog": 1.0, "cat": 8.321435096547702e-09, "automobile": 6.151766651640855e-09, "bird": 4.842380940672797e-10, "dog": 2.1843146735811558e-10}
predicted label: frog
done testing: frog.png
_____________________________________________________
response: {"horse": 0.9999997615814209, "dog": 1.8233293985758792e-07, "deer": 2.948480760760208e-13, "bird": 7.617125890267955e-15, "airplane": 1.0709949171345602e-15}
predicted label: horse
done testing: horse.png
_____________________________________________________
response: {"automobile": 0.9891622066497803, "ship": 0.010759363882243633, "airplane": 7.36139336368069e-05, "bird": 2.0724978639918845e-06, "dog": 1.3870318298359052e-06}
predicted label: automobile
done testing: 10054_automobile.png
_____________________________________________________
[32mPASSED[0m

============================== slowest durations ===============================
0.49s call     test_serve/test_serve_cifar.py::test_cifar_inference[35.78.219.103]

(2 durations < 0.005s hidden.  Use -vv to show these durations.)
[32m============================== [32m[1m1 passed[0m[32m in 1.11s[0m[32m ===============================[0m
