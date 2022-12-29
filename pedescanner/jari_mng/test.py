import unittest
import pedescanner.jari_mng.vehicle_info as vehicle_info

record_name = "03_20160119_174003"

class TestJariMethods(unittest.TestCase):
    
    def test_read_vehicle_data(self):
        df = vehicle_info.read_vehicle_data(record_name)
        self.assertEqual(df.shape[1], 9)
        df = vehicle_info.read_vehicle_data(record_name, sel_fields=["time", "x_accel"])
        self.assertEqual(df.shape[1], 2)

    def test_plot_data(self):
        df = vehicle_info.read_vehicle_data(record_name)
        vehicle_info.plot_data(df.head(2000), x_field="time", y_field=["x_vel", "accel_pedal", "brake_pedal"])

if __name__ == "__main__":
    unittest.main()