def running_average():
    data = {"sum" : 0, "ctr" : 0};
    def f(num):
        data["sum"] += num;
        data["ctr"] += 1;
        return round(data["sum"] * 1.0 / data["ctr"], 2);
    return f;