import unittest
from inkycal.modules import Slideshow as Module
from inkycal.custom import top_level

test_path = f'{top_level}/Gallery'

tests = [
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [400,200],
    "path": test_path,
    "palette": "bwy",
    "autoflip": True,
    "orientation": "vertical",
    "padding_x": 10, "padding_y": 10, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [800,500],
    "path": test_path,
    "palette": "bw",
    "autoflip": True,
    "orientation": "vertical",
    "padding_x": 10, "padding_y": 10, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [400,100],
    "path": test_path,
    "palette": "bwr",
    "autoflip": False,
    "orientation": "vertical",
    "padding_x": 10, "padding_y": 10, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [400,100],
    "path": test_path,
    "palette": "bwy",
    "autoflip": True,
    "orientation": "vertical",
    "padding_x": 10, "padding_y": 10, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [400,100],
    "path": test_path,
    "palette": "bwy",
    "autoflip": True,
    "orientation": "horizontal",
    "padding_x": 10, "padding_y": 10, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [500, 800],
    "path": test_path,
    "palette": "bw",
    "autoflip": True,
    "orientation": "vertical",
    "padding_x": 0, "padding_y": 0, "fontsize": 12, "language": "en"
    }
},
{
  "position": 1,
  "name": "Slideshow",
  "config": {
    "size": [500, 800],
    "path": test_path,
    "palette": "bwr",
    "autoflip": True,
    "orientation": "vertical",
    "padding_x": 20, "padding_y": 20, "fontsize": 12, "language": "en"
    }
},
]

class module_test(unittest.TestCase):
  def test_get_config(self):
    print('getting data for web-ui...', end = "")
    Module.get_config()
    print('OK')

  def test_generate_image(self):
    for test in tests:
      print(f'test {tests.index(test)+1} generating image..')
      module = Module(test)
      module.generate_image()
      print('OK')

  def test_switch_to_next_image(self):
    print(f'testing switching to next images..')
    module = Module(tests[0])
    module.generate_image()
    module.generate_image()
    module.generate_image()
    print('OK')

if __name__ == '__main__':
  unittest.main()