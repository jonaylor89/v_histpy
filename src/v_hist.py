#!/usr/bin/env bash

from typing import List
from random import randint

class Histogram(object):

    def __init__(self):
        self.labels: List[str] = []
        self.values: List[str] = []

    def add(self, label: str, value: int):
        labels.append(label)
        values.append(value)

    def show(self):
        pass

    def draw(self, values: List[int]):
        for i, value in enumerate(values):
            self.add(f"{i}", value)

        self.show()
    

def main():
   h = Histogram()
   
   h.draw([randint(0, 3000) for x in range(200)])

if __name__ == '__main__':
    main()
