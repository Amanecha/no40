# Contributing to no40

&nbsp; First of all, thank you for trying to contribute! This guide explains how to report bugs, suggest new features, and contribute code.  
(まずは、貢献しようとしていただきありがとうございます！このガイドでは、バグ報告や新しい機能提案、コードの貢献方法について説明します。)

---

## Bug report(バグ報告)

&nbsp; If you find a bug, please report it using the following steps:  
(バグを見つけた場合は、以下の手順で報告してください：)

1. **Search issue**: Please check if the same bug has already been reported.  
(既に同じバグが報告されていないか確認してください。)

2. **Create a new issue**: If the bug has not yet been reported, please create a new issue from the Issues (insert link) tab.  
(バグが未報告の場合、[Issues](https://github.com/Amanecha/no40/issues)タブから新しいIssueを作成してください。)
   - **title**: Please provide a brief summary of the bug.  
   (バグの概要を簡潔に記載してください。)
   - **contents**: Please provide details in the format below:  
   (以下のフォーマットで詳細を記載してください：)
     ```
     ### Bug Summary(バグの概要)
     - What's the problem?(何が問題ですか？)

     ### Steps to reproduce(再現手順)
     1. Step 1(手順1)
     2. Step 2(手順2)
     3. Step 3(手順3)
     
     ### Expected results(期待される結果)
     - Please briefly explain normal behavior.(正常な挙動を簡単に説明してください。)
     
     ### enviroment infomation
     - OS: [ex.: Windows 11 / macOS Ventura]
     - Pythonバージョン: [ex.: 3.10.7]
     - Other dependencies: [Describe if necessary] 
     (その他依存関係: [必要であれば記載])
     ```

---

## フィーチャーリクエスト

&nbsp; Suggestions for new features are welcome! Please follow these steps to submit your request:  
(新しい機能の提案を歓迎します！以下の手順でリクエストを提出してください：)

1. **Search issue**: Please check if there is already a similar request.  
(既に同様のリクエストがあるか確認してください。)
2. **Create new issue**: [Issues](https://github.com/Amanecha/no40/issues) tab, create an issue with the label `Feature Request`.
(リンクから、`Feature Request`のラベルを付けてIssueを作成してください。)
   - **title**: A concise summary of the proposed functionality.  
   (提案する機能の概要を簡潔に記載。)
   - **contents**: Please provide details in the following format:  
   (以下のフォーマットで詳細を記載してください：)
     ```
     ### Feature Overview (機能の概要)
     - What features would you like to add?
     (どのような機能を追加したいですか？)

     ### Use case (ユースケース)
     - Please tell me specifically when to use this function.
     (この機能を使用する場面を具体的に教えてください。)

     ### Other things to consider (他に考慮すべきこと)
     - Other related features and compatibility concerns, etc.
     (他の関連機能や互換性についての懸念など。)
     ```

---

## Pull Request (プルリクエスト)

If you would like to contribute code, please follow these steps:  
(コードに貢献してくれる場合は、以下の手順を守ってください：)

1. **Check the issue**: If associated with an existing issue, please record the issue number.  
(既存のIssueに関連付けられる場合、そのIssue番号を記録してください。)
2. **フォークとブランチ**:
   - Fork this repository. (このリポジトリをフォークします。)
   - Please create a new branch. (新しいブランチを作成してください（ex.: `feature/add-new-feature`）。)
3. **Code changes**:
   - It is possible to make changes according to your coding style.  
   (コーディングスタイルに従って変更を加えることが可能です。)
   - Add tests as needed.  
   (必要に応じてテストを追加します。)
4. **Create a pull request**:
   - Include a concise summary in the pull request title.
   プルリクエストのタイトルには簡潔な概要を記載します。
   - Please include the following in the description field:
   説明欄には以下を記載してください：
     ```
     ### Related Issues
     - Issue number: #123 
     (Issue番号: #123)
     
     ### Changes
     - Please briefly explain the changes you made in this PR.
     (このPRで行った変更を簡潔に説明してください。)

     ### test
     - Please describe the tests you performed and their results.
     (実行したテストやその結果を記載してください。)
     ```

---

## coding style (コーディングスタイル)

Please consider the style guide below:  
(以下のスタイルガイドを考慮してください：)
- **Python**: Please comply with PEP8.(PEP8に準拠してください。)
- **Naming convention**: Keep variable and function names clear and concise.(変数名や関数名はわかりやすく簡潔に。)
- **comment**: Add explanatory comments to the code where necessary.(必要に応じてコードに説明コメントを記載。)


Before changing your code, use the `pre-commit` hook to perform static analysis:  
(コードを変更する前に、`pre-commit`フックを使って静的解析を実行してください：)

```bash
pre-commit install
pre-commit run --all-files
