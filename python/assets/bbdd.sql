CREATE TABLE users (
  id          INTEGER AUTO_INCREMENT PRIMARY KEY,
  username    VARCHAR(100) UNIQUE,
  password    VARCHAR(100),
  role        VARCHAR(10) DEFAULT 'USER'
);

CREATE TABLE pcs (
  id        INTEGER AUTO_INCREMENT PRIMARY KEY ,
  ref_user  INTEGER REFERENCES users(id),
  mac       VARCHAR(24), -- ya
  pc_name   VARCHAR(50) -- ya
);

CREATE TABLE pc_data (
  ref_pc      INTEGER REFERENCES pcs(id),
  ram         BIGINT,       -- ya
  cpu_name    VARCHAR(100), -- ya
  cores       TINYINT,    -- ya
  threads     TINYINT,    -- ya
  so          varchar(50), -- ya
  so_v        varchar(100), -- ya
  hdd         BIGINT, -- ya
  ip_priv     VARCHAR(20),        -- ya
  ip_pub      VARCHAR(40)         /* para ipv6 */
);

CREATE TABLE cpu_stat (
  ref_pc      INTEGER REFERENCES pcs(id),
  user_us     DOUBLE,
  sys_us      DOUBLe,
  unused      DOUBLE,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat)
);
CREATE TABLE cpu_details_stat (
  ref_pc    INTEGER AUTO_INCREMENT REFERENCES pcs(id),
  num_cpu   INT(3),
  user_us   DOUBLE,
  sys_us    DOUBLe,
  unused    DOUBLE,
  perc_us   DOUBLE,
  date_stat DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,num_cpu,date_stat)
);

CREATE TABLE ram_stat (
  ref_pc      INTEGER REFERENCES pcs(id),
  used        BIGINT,
  available   BIGINT,
  free        BIGINT,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat)
);

CREATE TABLE disk_stat (
  ref_pc      INTEGER AUTO_INCREMENT REFERENCES pcs(id),
  disk_path   VARCHAR(7),
  used        BIGINT,
  free        BIGINT,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,disk_path,date_stat)
);



CREATE TABLE net_stat (
  ref_pc      INTEGER REFERENCES pcs(id),
  bytes_sent  BIGINT,
  bytes_recv  BIGINT,
  pack_sent   BIGINT,
  pack_recv   BIGINT,
  balance     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat)
);


CREATE TABLE net_details_stat (
  ref_pc      INTEGER REFERENCES pcs(id),
  type_net    VARCHAR(150),
  bytes_sent  BIGINT,
  bytes_recv  BIGINT,
  pack_sent   BIGINT,
  pack_recv   BIGINT,
  date_stat   DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,type_net,date_stat)
);


CREATE TABLE process(
  ref_pc      INTEGER REFERENCES pcs(id),
  pid        INTEGER,
  proc_name   VARCHAR(80),
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc, pid, date_stat)
);