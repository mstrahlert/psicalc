#!/usr/bin/env python

import argparse

def tire_width(argument):
  width = int(argument)
  if width < 19 or width > 45:
    raise argparse.ArgumentTypeError("{} not within parameters".format(argument))
  return width

def kg2lbs(kg):
  return kg * 2.20462

def psi2bar(psi):
  return psi * 0.06895

def drop_formula(load, width):
  return 600 * load / (width * width) + 0.75 * width - 25

def main():
  parser = argparse.ArgumentParser(description='PSI Calculator')
  #parser.add_argument('--unit', default='psi', choices=['psi', 'bar'])
  parser.add_argument('--ratio', default=1.0, type=float,
      help='Skew results (default: %(default)s)')
  parser.add_argument('--load', default=50, type=int,
      help='Percent of weight distribution on back wheel (default: %(default)s)')
  parser.add_argument('weight', type=float, help='Weight in Kg (rider + bike)')
  parser.add_argument('width', type=tire_width, help='Width of tyre in mm')

  results = parser.parse_args()

  #back = drop_formula(kg2lbs((results.weight * results.load) / 100.0), results.width)
  back = drop_formula(kg2lbs((results.weight / 2) * (results.load * 2 / 100.0)), results.width)
  back *= results.ratio
  #front = drop_formula(kg2lbs((results.weight * (100 - results.load)) / 100.0), results.width)
  front = drop_formula(kg2lbs((results.weight / 2) / (results.load * 2 / 100.0)), results.width)
  front *= results.ratio
  
  print("Back  PSI: {:.0f}, Bar: {:.1f}".format(back, psi2bar(back)))
  print("Front PSI: {:.0f}, Bar: {:.1f}".format(front, psi2bar(front)))

if __name__ == "__main__":
  main()
