CREATE TABLE users (
  id          INTEGER AUTO_INCREMENT PRIMARY KEY,
  username    VARCHAR(100) UNIQUE,
  password    VARCHAR(100),
  role        VARCHAR(10) DEFAULT 'USER'
);

CREATE TABLE pcs (
  id        INTEGER AUTO_INCREMENT PRIMARY KEY ,
  ref_user  INTEGER,
  mac       VARCHAR(24), -- ya
  pc_name   VARCHAR(50), -- ya
  CONSTRAINT FOREIGN KEY (ref_user) REFERENCES users(id)
);

CREATE TABLE pc_data (
  ref_pc      INTEGER PRIMARY KEY,
  ram         BIGINT,       -- ya
  cpu_name    VARCHAR(100), -- ya
  cores       TINYINT,    -- ya
  threads     TINYINT,    -- ya
  so          varchar(50), -- ya
  so_v        varchar(100), -- ya
  hdd         BIGINT,-- ya
  ip_priv     VARCHAR(20),        -- ya
  ip_pub      VARCHAR(40) ,        /* para ipv6 */
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);

CREATE TABLE cpu_stat (
  ref_pc      INTEGER,
  user_us     DOUBLE,
  sys_us      DOUBLe,
  unused      DOUBLE,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);
CREATE TABLE cpu_details_stat (
  ref_pc    INTEGER,
  num_cpu   INT(3),
  user_us   DOUBLE,
  sys_us    DOUBLe,
  unused    DOUBLE,
  perc_us   DOUBLE,
  date_stat DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,num_cpu,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);

CREATE TABLE ram_stat (
  ref_pc      INTEGER,
  used        BIGINT,
  available   BIGINT,
  free        BIGINT,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);

CREATE TABLE disk_stat (
  ref_pc      INTEGER,
  disk_path   VARCHAR(30),
  used        BIGINT,
  free        BIGINT,
  perc_us     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,disk_path,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);



CREATE TABLE net_stat (
  ref_pc      INTEGER,
  bytes_sent  BIGINT,
  bytes_recv  BIGINT,
  pack_sent   BIGINT,
  pack_recv   BIGINT,
  balance     DOUBLE,
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);


CREATE TABLE net_details_stat (
  ref_pc      INTEGER,
  type_net    VARCHAR(150),
  bytes_sent  BIGINT,
  bytes_recv  BIGINT,
  pack_sent   BIGINT,
  pack_recv   BIGINT,
  date_stat   DATETIME,
  CONSTRAINT PRIMARY KEY (ref_pc,type_net,date_stat),
  CONSTRAINT FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);


CREATE TABLE process(
  ref_pc      INTEGER,
  pid         INTEGER,
  proc_name   VARCHAR(80),
  date_stat   DATETIME,
  CONSTRAINT  PRIMARY KEY (ref_pc, pid, date_stat),
  CONSTRAINT  FOREIGN KEY (ref_pc) REFERENCES pcs(id)
);