class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

chicken = 10
waiting = 1
while(True):
    print("남은 치킨 : {0}".format(chicken))
    try:
        order = int(input("치킨 몇 마리를 주문하시겠습니까? :"))
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
        continue

    try:
        if order > chicken:
            print("재료가 부족합니다.")
            raise SoldOutError("재료가 소진되어서 더이상의 주문은 받지 않습니다.")
        else:
            print(f"[대기번호 {waiting}] {order}마리의 치킨을 주문하셨습니다.")
            waiting += 1
            chicken -= order
    except SoldOutError as err:
        print(err)
        break;