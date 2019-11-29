class Drink:

    COKE = 0
    DIET_COKE = 1
    TEA = 2

    def __init__(self, kind):
        self._kind = kind

    @property
    def kind(self):
        return self._kind


class VendingMachine:

    # コーラの在庫数
    quantityOfCoke = 5

    # ダイエットコーラの在庫数
    quantityOfDietCoke = 5

    # お茶の在庫数
    quantityOfTea = 5

    # 100円玉の在庫
    numberOf100Yen = 10

    # お釣り
    charge = 0

    def buy(self, i, kindOfDrink):
        """購入する

        Arguments:
            i {int} -- 投入金額. 100円と500円のみ受け付ける.
            kindOfDrink {int} -- ジュースの種類.
                    コーラ({@code Juice.COKE}),ダイエットコーラ({@code Juice.DIET_COKE},お茶({@code Juice.TEA})が指定できる.
        Returns:
            Drink-- 指定したジュース. 在庫不足や釣り銭不足で買えなかった場合は {@code null} が返される.
        """
        if i != 100 and i != 500:
            self.charge += i
            return None
        if kindOfDrink == Drink.COKE and self.quantityOfCoke == 0:
            self.charge += i
            return None
        elif kindOfDrink == Drink.DIET_COKE and self.quantityOfDietCoke == 0:
            self.charge += i
            return None
        elif kindOfDrink == Drink.TEA and self.quantityOfTea == 0:
            self.charge += i
            return None

        # 釣り銭不足
        if i == 500 and self.numberOf100Yen < 4:
            self.charge += i
            return None

        if i == 100:
            # 100円玉を釣り銭に使える
            self.numberOf100Yen += 1
        elif i == 500:
            # 400円のお釣り
            self.charge += (i - 100)
            # 100円玉を釣り銭に使える
            self.numberOf100Yen -= (i - 100) / 100

        if kindOfDrink == Drink.COKE:
            self.quantityOfCoke -= 1
        elif kindOfDrink == Drink.DIET_COKE:
            self.quantityOfDietCoke -= 1
        else:
            self.quantityOfTea -= 1

        return Drink(kindOfDrink)

    def refund(self):
        """お釣りを取り出す

        Returns:
            int-- お釣りの金額
        """
        result = self.charge
        self.charge = 0
        return result
