import fire

class OC2(object):
  """A simple CLi class."""

  def name(self, number):
    return "oc2"

if __name__ == '__main__':
  fire.Fire(OC2)
