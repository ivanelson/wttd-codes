#-*- encoding: utf-8 -*-

"""

Jogo FizzBuzz

Quando o n£mero for multiplo de 3, fala fizz;
Quando o n£mero for multiplo de 5, fala buzz;
Quando o n£mero for multiplo de 3 e 5, fala fizzbuzz;
Para os demais diga o pr¢prio n£mero;

"""
from functools import partial


multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say


if __name__ == "__main__":
    print ("Run tests...")
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
