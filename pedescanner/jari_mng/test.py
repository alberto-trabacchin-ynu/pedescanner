import unittest
import pedescanner.jari_mng.vehicle_info as vehicle_info

record_name = "05_20151023_165310"

class TestJariMethods(unittest.TestCase):
    
    def test_read_vehicle_data(self):
        df = vehicle_info.read_vehicle_data(record_name)
        self.assertEqual(df.shape[1], 9)
        print(df.head(10))
        df = vehicle_info.read_vehicle_data(record_name, sel_fields=["time", "x_accel"])
        self.assertEqual(df.shape[1], 2)

    def test_get_init_time_format(self):
        init_time = vehicle_info.get_init_time_format(record_name)
        self.assertEqual(len(init_time), 21)

    @unittest.skip("Temp")
    def test_plot_data(self):
        df = vehicle_info.read_vehicle_data(record_name)
        vehicle_info.plot_data(df, x_field="time", y_fields=["x_vel", "accel_pedal", "brake_pedal"], normalize=True)

if __name__ == "__main__":
    unittest.main()