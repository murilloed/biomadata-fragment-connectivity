import unittest
from shapely.geometry import box
from analysis import connectivity
class GraphTests(unittest.TestCase):
 def test_connected_chain_and_minimum_weight(self):
  f=[box(0,0,1,1),box(3,0,4,1),box(7,0,8,1)]
  r=connectivity(f,10)
  self.assertEqual(r['component_count'],1)
  self.assertEqual(len(r['minimum_spanning_forest']),2)
  self.assertAlmostEqual(r['total_gap_m'],5)
 def test_disconnected_threshold_and_touching(self):
  f=[box(0,0,1,1),box(3,0,4,1),box(7,0,8,1)]
  self.assertEqual(connectivity(f,2)['component_count'],2)
  self.assertEqual(connectivity([box(0,0,1,1),box(1,0,2,1)],0)['component_count'],1)
 def test_empty_and_invalid_threshold(self):
  self.assertEqual(connectivity([],1)['component_count'],0)
  with self.assertRaises(ValueError):connectivity([],float('nan'))
