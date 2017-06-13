'''
Author: Xavier Maldonado
Instructor: Dr. Klump
Object-Oriented Programming
April 11, 2016
'''

from math import radians, cos, sin, asin, sqrt

'''
Calculates the distance between two points
on the earth (specified in decimal degrees).
'''

class GPS_Calculator:

    # calc_distance returns the distance between the two points in miles
    def calc_distance(lon1, lat1, lon2, lat2):
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        km = 6367 * c
        mi = km * 0.621371
        mi = "{0:.3f}".format(mi)
        return mi

    # calc_time returns the pace, (min/mile)
    def calc_time(time1, time2, dist):
        time1 = time1.split(":")
        hh1 = int(time1[0])
        mm1 = int(time1[1])
        ss1 = int(time1[2])
        second_time1 = (hh1 * 3600) + (mm1 * 60) + ss1

        time2 = time2.split(":")
        hh2 = int(time2[0])
        mm2 = int(time2[1])
        ss2 = int(time2[2])
        second_time2 = (hh2 * 3600) + (mm2 * 60) + ss2

        total_time_sec = second_time2 - second_time1
        total_time_min = total_time_sec / 60

        dist = float(dist)
        pace = total_time_min / dist
        pace = "{0:.3f}".format(pace)
        return pace

    # calc_best_speed returns a tuple containing fastest pace in minutes with seconds.
    # (from a list that contains floats)
    def calc_best_speed(pace_list):
        best_speed = min(pace_list)

        time = best_speed / 60
        minutes = round((time * 60) % 60)
        seconds = round((time * 3600) % 60)

        return minutes, seconds

'''
Report_Printer includes a function to read in a file and prints a nicely formatted report based
on GPS data.
'''

class Report_Printer:

    def print_result(self):
        print("Welcome to Running mate")
        filename = input("Enter name of data file: ").strip()

        print("-" * 70)
        print("Time         Latitude          Longitude    Distance       Pace")
        print("(hh:mm:ss    (deg)             (deg)        (miles)        (min/mile)")
        print("-" * 70)

        first = True
        f = open(filename, 'r')
        for line in f:
            if first is True:
                pace_list = []
                info = line.strip().split(" ")
                time1 = info[0]
                lat1 = float(info[1])
                lon1 = float(info[2])
                dist = "*****"
                pace = "*****"

                print(time1, "   ", lat1, "    ", lon1, "     ", dist, "        ", pace)
                first = False
            else:
                info = line.strip().split(" ")

                time2 = info[0]
                lat2 = float(info[1])
                lon2 = float(info[2])
                lon_str = info[2]

                dist = GPS_Calculator.calc_distance(lon1, lat1, lon2, lat2)
                pace = GPS_Calculator.calc_time(time1, time2, dist)
                pace_list.append(float(pace))

                print(time2, "   ", lat2, "    ", lon_str, "     ", dist, "        ", pace)
                lat1 = lat2
                lon1 = lon2
                time1 = time2

        f.close()
        best_min, best_sec = GPS_Calculator.calc_best_speed(pace_list)
        print("-" * 70)
        print("Your fastest speed was", best_min, " minutes and ", best_sec, " seconds per mile.")


# below is an object of the Report_Printer class to actually produce the report.
def main():
    rp = Report_Printer()
    rp.print_result()

if __name__ == "__main__":
    main()
