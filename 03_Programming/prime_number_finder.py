"""
소수 찾기 프로그램
Prime Number Finder Program

작성자: jylee2930
작성일: 2025-08-30
"""

import math
import time
from typing import List


def is_prime_basic(n: int) -> bool:
    """
    기본적인 소수 판별 함수
    
    Args:
        n (int): 판별할 숫자
        
    Returns:
        bool: 소수이면 True, 아니면 False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 3부터 sqrt(n)까지 홀수만 확인
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_prime_optimized(n: int) -> bool:
    """
    최적화된 소수 판별 함수
    
    Args:
        n (int): 판별할 숫자
        
    Returns:
        bool: 소수이면 True, 아니면 False
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 6k±1 형태의 수만 확인 (더 효율적)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_in_range(start: int, end: int) -> List[int]:
    """
    범위 내의 모든 소수 찾기
    
    Args:
        start (int): 시작 숫자
        end (int): 끝 숫자
        
    Returns:
        List[int]: 소수 리스트
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime_optimized(num):
            primes.append(num)
    return primes


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    에라토스테네스의 체를 이용한 소수 찾기 (대용량 처리에 효율적)
    
    Args:
        limit (int): 찾을 소수의 상한
        
    Returns:
        List[int]: 소수 리스트
    """
    if limit < 2:
        return []
    
    # 모든 수를 소수로 가정
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            # i의 배수들을 모두 제거
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # 소수만 추출
    return [num for num in range(2, limit + 1) if is_prime[num]]


def find_nth_prime(n: int) -> int:
    """
    n번째 소수 찾기
    
    Args:
        n (int): 찾을 소수의 순서
        
    Returns:
        int: n번째 소수
    """
    if n < 1:
        raise ValueError("n은 1 이상이어야 합니다.")
    
    count = 0
    num = 2
    
    while count < n:
        if is_prime_optimized(num):
            count += 1
            if count == n:
                return num
        num += 1
    
    return num


def prime_factorization(n: int) -> List[int]:
    """
    소인수분해
    
    Args:
        n (int): 소인수분해할 숫자
        
    Returns:
        List[int]: 소인수 리스트
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


def benchmark_prime_functions(limit: int = 10000):
    """
    소수 찾기 함수들의 성능 비교
    
    Args:
        limit (int): 테스트할 숫자의 상한
    """
    print(f"=== 소수 찾기 성능 비교 (1 ~ {limit}) ===\n")
    
    # 기본 함수 테스트
    start_time = time.time()
    primes_basic = [n for n in range(2, limit + 1) if is_prime_basic(n)]
    basic_time = time.time() - start_time
    
    # 최적화 함수 테스트
    start_time = time.time()
    primes_optimized = [n for n in range(2, limit + 1) if is_prime_optimized(n)]
    optimized_time = time.time() - start_time
    
    # 에라토스테네스의 체 테스트
    start_time = time.time()
    primes_sieve = sieve_of_eratosthenes(limit)
    sieve_time = time.time() - start_time
    
    print(f"기본 함수:      {len(primes_basic):5d}개 소수, {basic_time:.4f}초")
    print(f"최적화 함수:    {len(primes_optimized):5d}개 소수, {optimized_time:.4f}초")
    print(f"에라토스테네스: {len(primes_sieve):5d}개 소수, {sieve_time:.4f}초")
    
    # 성능 향상 계산
    if basic_time > 0:
        print(f"\n최적화 함수는 기본 함수보다 {basic_time/optimized_time:.1f}배 빠름")
        print(f"에라토스테네스는 기본 함수보다 {basic_time/sieve_time:.1f}배 빠름")


def main():
    """메인 함수 - 프로그램 실행"""
    print("🔢 소수 찾기 프로그램")
    print("=" * 50)
    
    while True:
        print("\n메뉴를 선택하세요:")
        print("1. 특정 숫자가 소수인지 확인")
        print("2. 범위 내 모든 소수 찾기")
        print("3. n번째 소수 찾기")
        print("4. 소인수분해")
        print("5. 에라토스테네스의 체로 소수 찾기")
        print("6. 성능 비교 테스트")
        print("0. 종료")
        
        try:
            choice = int(input("\n선택: "))
            
            if choice == 0:
                print("프로그램을 종료합니다.")
                break
                
            elif choice == 1:
                num = int(input("확인할 숫자를 입력하세요: "))
                result = is_prime_optimized(num)
                print(f"{num}은(는) {'소수입니다' if result else '소수가 아닙니다'}.")
                
            elif choice == 2:
                start = int(input("시작 숫자: "))
                end = int(input("끝 숫자: "))
                primes = find_primes_in_range(start, end)
                print(f"\n{start}부터 {end}까지의 소수:")
                print(primes)
                print(f"총 {len(primes)}개의 소수가 있습니다.")
                
            elif choice == 3:
                n = int(input("몇 번째 소수를 찾을까요? "))
                nth_prime = find_nth_prime(n)
                print(f"{n}번째 소수는 {nth_prime}입니다.")
                
            elif choice == 4:
                num = int(input("소인수분해할 숫자를 입력하세요: "))
                factors = prime_factorization(num)
                print(f"{num}의 소인수분해: {' × '.join(map(str, factors))}")
                
            elif choice == 5:
                limit = int(input("몇까지의 소수를 찾을까요? "))
                start_time = time.time()
                primes = sieve_of_eratosthenes(limit)
                elapsed_time = time.time() - start_time
                print(f"\n1부터 {limit}까지의 소수:")
                if len(primes) <= 100:  # 100개 이하일 때만 전체 출력
                    print(primes)
                else:
                    print(f"처음 10개: {primes[:10]}")
                    print(f"마지막 10개: {primes[-10:]}")
                print(f"총 {len(primes)}개의 소수를 {elapsed_time:.4f}초에 찾았습니다.")
                
            elif choice == 6:
                limit = int(input("테스트할 범위 (기본값 10000): ") or "10000")
                benchmark_prime_functions(limit)
                
            else:
                print("잘못된 선택입니다. 다시 입력해주세요.")
                
        except ValueError:
            print("올바른 숫자를 입력해주세요.")
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
