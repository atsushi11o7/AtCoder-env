# AtCoder の問題に対する解答のエントリーポイント

def main():
    # 入力
    S = input().strip()  # 文字列入力
    N = int(input().strip())  # 整数入力
    N, M = map(int, input().split())  # 整数入力２
    X = float(input().strip())  # 小数入力
    C = [input().strip() for _ in range(N)]  # N個の文字列の入力
    A = list(map(int, input().split()))  # 整数列
    N, Q = map(int, input().split())  # 複数の入力が一度にある場合
    
    # 問題解決のための処理
    result = solve(data)

    print(result)

def solve(data):
    """
    問題解決のロジックを実装する
    """
    # 入力された単語を空白区切りで再結合して返す例
    return result

if __name__ == "__main__":
    main()