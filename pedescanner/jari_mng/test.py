import unittest
import pedescanner.jari_mng.vehicle_info as vehicle_info

class TestJariMethods(unittest.TestCase):
    
    def test_read_vehicle_data(self):
        df = vehicle_info.read_vehicle_data("03_20160119_174003")
        n_features = df.shape[1]
        self.assertEqual(n_features, 9)

if __name__ == "__main__":
    unittest.main()