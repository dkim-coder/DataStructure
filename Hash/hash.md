# Hash Table: List or Array (index 갖고 value 저장 가능)
1. 매우 빠른 평균 삽입, 삭제, 탐색 연산 제공 O(1)
2. key 값을 해시 함수를 활용해 index mapping -> hash_func(key) > return index
3. Hash function < 충돌이 적어야 좋다. > < 연산이 빨라야 한다. > tradeoff 관계
4. Collision resolution method (충돌회피방법)필요
