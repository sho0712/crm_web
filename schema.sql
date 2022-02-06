-- テーブルが存在していたら削除
DROP TABLE IF EXISTS customers;

-- テーブルがなかったら作成
CREATE TABLE IF NOT EXISTS customers(
   place TEXT,
   temperature INTEGER
);

-- テストデータ挿入
INSERT INTO customers

VALUES
  ( '平泉',15),
  ( '一関',57),
  ( '仙台',76)
 ;

