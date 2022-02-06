-- テーブルが存在していたら削除
DROP TABLE IF EXISTS customers;

-- テーブルがなかったら作成
CREATE TABLE IF NOT EXISTS customers(
   name TEXT,
   age INTEGER
);

-- テストデータ挿入
INSERT INTO customers

VALUES
  ('Bob',15),
  ('Tom',57),
  ('Ken',76)
 ;

