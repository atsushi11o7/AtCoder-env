# AtCoder-env
AtCoder用ディレクトリ

## ディレクトリ構成
atcoder-env/
├── README.md          // リポジトリの概要、利用方法、環境構築手順の概要
├── docs/              // 詳細なドキュメント（セットアップ手順、言語ごとのガイドなど）
│   └── setup.md       
├── templates/         // 各言語のテンプレートコード
│   ├── cpp/
│   │   └── main.cpp   // C++ の基本テンプレート
│   ├── python/
│   │   └── main.py    // Python の基本テンプレート
│   └── java/
│       └── Main.java  // Java の基本テンプレート
├── solutions/         // 各コンテストの解答コードを管理
│   ├── cpp/
│   │   ├── ABC/       // ABCコンテスト用の解答例（C++）
│   │   └── ARC/       // ARCコンテスト用の解答例（C++）
│   ├── python/
│   │   ├── ABC/       
│   │   └── ARC/
│   └── java/
│       ├── ABC/
│       └── ARC/
├── scripts/           // コンパイル、実行、テストの自動化スクリプト
│   ├── build_cpp.sh   // C++ のビルドスクリプト
│   ├── run_python.sh  // Python の実行スクリプト
│   └── build_java.sh  // Java のビルドスクリプト
├── tests/             // ローカルでのテストケース、サンプル入出力ファイル
│   ├── problem1/
│   │   ├── input.txt
│   │   └── output.txt
│   └── problem2/
├── docker/            // Docker を用いる場合の設定ファイル
│   └── Dockerfile
└── .gitignore         // 各言語のビルド成果物やエディタ設定など不要なファイルを除外
