class Person:
    def __init__(self, name_param):
        # 객체가 생성될때 호출되는 함수, 여기에 속성을 넣으면 속성값을 가질 수 있다.
        # self는 자기 자신을 가르킴.
        self.name = name_param
        print("I'm created!", self, self.name)

    pass # 여기서 pass 는 안에 아무런 내용이 없다는 의미입니다!

    def talk(self):
        # self는 자기 자신을 가리킬 뿐이라 호출시 파라미터를 넘겨주지 않아도 됨.
        print("안녕하세요 저는", self.name, "입니다.")

person_1 = Person("유재석")
person_1.talk()
person_2 = Person("박명수")
person_2.talk()