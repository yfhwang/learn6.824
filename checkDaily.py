import datetime
import os

members = {
    "huangjunqing": "XiaoZhuo_Ops",
    "yangchh": "yangchh1998",
    "ivan": "zjrenivan",
    "SimhaZF": "ZSimha",
    "rookie0080": "rookie0080"
}
checklist = list(members.keys())


def check(days_before):
    print(os.getcwd())
    today = datetime.date.today()
    day = today - datetime.timedelta(days=days_before)

    path_day = os.path.join(os.getcwd(), "homework", day.strftime('%Y%m'), day.strftime('%m%d'))

    for _, _, files in os.walk(path_day):
        for file in files:
            for member in checklist:
                if member in file:
                    checklist.remove(member)
    return [members[i] for i in checklist]


if __name__ == "__main__":
    l1 = check(1)
    l2 = check(4)
    ll = []
    for m in l1:
        if m in l2:
            ll.append(m)
    print(ll)

