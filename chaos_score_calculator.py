import os

def first_ok(paths):
    for p in paths:
        if p and os.path.isdir(p):
            return p
    return None

def file_count(folder):
    if not folder or not os.path.isdir(folder):
        return 0
    c = 0
    for name in os.listdir(folder):
        full = os.path.join(folder, name)
        if os.path.isfile(full):
            c += 1
    return c

def calc_score(count, limit):
    if count <= limit:
        return int(count * 30 / limit)
    elif count <= 2 * limit:
        extra = count - limit
        return 30 + int(extra * 50 / limit)
    elif count <= 3 * limit:
        extra = count - 2 * limit
        return 80 + int(extra * 20 / limit)
    else:
        return 100

def message4(score):
    if score < 25:
        return "Excellent - almost no chaos."
    elif score < 50:
        return "Not bad - a bit of tidying could help."
    elif score < 70:
        return "Chaos level is a bit high - tidying would help."
    else:
        return "Chaos level is high - time to clean!"

def main():
    home = os.path.expanduser("~")

    desktop = first_ok([os.path.join(home, "Desktop"),
                        os.path.join(home, "Masaüstü")])
    downloads = first_ok([os.path.join(home, "Downloads"),
                          os.path.join(home, "İndirilenler")])
    documents = first_ok([os.path.join(home, "Documents"),
                          os.path.join(home, "Belgeler")])

    DESK_LIMIT = 20
    DOWN_LIMIT = 50
    DOC_LIMIT  = 30

    d_cnt = file_count(desktop)
    w_cnt = file_count(downloads)
    c_cnt = file_count(documents)

    d_scr = calc_score(d_cnt, DESK_LIMIT)
    w_scr = calc_score(w_cnt, DOWN_LIMIT)
    c_scr = calc_score(c_cnt, DOC_LIMIT)

    total = int((d_scr + w_scr + c_scr) / 3)
    out_of_10 = int(total / 10)
    comment = message4(total)

    print("=== Chaos Score Calculator ===\n")
    print("Desktop  :", d_cnt, "files ->", d_scr, "/100")
    print("Downloads:", w_cnt, "files ->", w_scr, "/100")
    print("Documents:", c_cnt, "files ->", c_scr, "/100")
    print("--------------------------------")
    print("Total Chaos Score:", total, "/100  |  out of 10:", out_of_10, "/10")
    print(comment)

    f = open("chaos_report.txt", "w", encoding="utf-8")
    f.write("Chaos Score Report\n")
    f.write("------------------\n")
    f.write("Desktop  : " + str(d_cnt) + " files -> " + str(d_scr) + "/100\n")
    f.write("Downloads: " + str(w_cnt) + " files -> " + str(w_scr) + "/100\n")
    f.write("Documents: " + str(c_cnt) + " files -> " + str(c_scr) + "/100\n")
    f.write("Total Chaos Score: " + str(total) + "/100  |  out of 10: " + str(out_of_10) + "/10\n")
    f.write(comment + "\n")
    f.close()

if __name__ == "__main__":
    main()
