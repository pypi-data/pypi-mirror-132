---
---		ftsim106.sql
---
---		FTSIM	

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

-- This command deletes everything belonging to the project 106
-- (all tables have foreign keys referencing the project.prjid)
delete from project where prjid = 106;
	
INSERT INTO project VALUES(106, 22, 20, 25);
INSERT INTO ft VALUES(106, 'a' , 'FT',    2,    5);
INSERT INTO ft VALUES(106, 'k1', 'KP',    6,    1);
INSERT INTO ft VALUES(106, 'b' , 'FT',   12,    8);
INSERT INTO ft VALUES(106, 's' , 'LB',    2,   12);
INSERT INTO ft VALUES(106, 'x' , 'DB', NULL, NULL);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a01', 'a',  4,  4);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a02', 'a',  5,  4);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a03', 'a',  6,  4);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a04', 'a',  7,  4);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a06', 'a',  8,  4);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a07', 'a',  9,  4);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a08', 'a',  9,  5);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a09', 'a',  9,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a10', 'a',  8,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a12', 'a',  7,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a13', 'a',  6,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a14', 'a',  5,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a15', 'a',  4,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a16', 'a',  3,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a17', 'a',  3,  5);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'a18', 'a',  3,  4);

insert into lf(prjid,lfname,ftname,xkor,ykor,lftyp) values (106, 'k11', 'k1',  5,  3, NULL);
insert into lf(prjid,lfname,ftname,xkor,ykor,lftyp) values (106, 'k12', 'k1',  5,  2, NULL);
insert into lf(prjid,lfname,ftname,xkor,ykor,lftyp) values (106, 'k13', 'k1',  6,  2, 'KP');
insert into lf(prjid,lfname,ftname,xkor,ykor,lftyp) values (106, 'k14', 'k1',  7,  2, NULL);
insert into lf(prjid,lfname,ftname,xkor,ykor,lftyp) values (106, 'k15', 'k1',  7,  3, NULL);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b01', 'b', 10,  4);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b02', 'b', 11,  4);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b03', 'b', 11,  5);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b04', 'b', 11,  6);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b05', 'b', 11,  7);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b06', 'b', 11,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b07', 'b', 11,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b08', 'b', 11, 10);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b09', 'b', 11, 11);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b10', 'b', 10, 11);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b11', 'b',  9, 11);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b12', 'b',  9, 10);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b13', 'b',  9,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b14', 'b',  9,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 'b15', 'b',  9,  7);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's01', 's',  8, 10);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's02', 's',  7,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's03', 's',  7,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's04', 's',  7, 11);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's05', 's',  6,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's06', 's',  6,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's07', 's',  6, 11);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's08', 's',  5,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's09', 's',  5,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's10', 's',  5, 11);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's11', 's',  3, 12);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's12', 's',  4, 12);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's13', 's',  5, 12);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's14', 's',  6, 12);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's15', 's',  7, 12);

insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's16', 's',  3, 11);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's17', 's',  4, 11);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's18', 's',  3,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's19', 's',  4,  9);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's20', 's',  3,  8);
insert into lf(prjid,lfname,ftname,xkor,ykor) values ( 106, 's21', 's',  4,  8);

insert into lfalt values  ( 106, 'a18', 'a01');

insert into lfalt values  ( 106, 'a02', 'k11');
insert into lfalt values  ( 106, 'k15', 'a04');

insert into lfalt values  ( 106, 'a07', 'b01');
insert into lfalt values  ( 106, 'b15', 'a09');

insert into lfalt values  ( 106, 'b12', 's01');
insert into lfalt values  ( 106, 's01', 'b12');

insert into lfziel values ( 106, 'k11', 'k1');

insert into lfziel values ( 106, 'b01', 'b' );
insert into lfziel values ( 106, 'b01', 's' );
insert into lfziel values ( 106, 'a09', 'b' );

insert into lfziel values ( 106, 's01', 's' );

insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L01', 's02', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L02', 's04', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L03', 's12', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L04', 's15', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L05', 's20', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L06', 's09', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L07', 's18', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L08', 's07', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L09', 's17', NULL);

insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L11', 'a01', NULL);
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L12', 'b07', 'b' );
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L13', 'b09', 's' );
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L14', 'a10', 's' );
insert into le(prjid,leid, lfname, ftziel) values ( 106, 'L15', 'a15', 's' );

-- lf.leid is deciding, le.leid is for convenience only
update lf set leid = (select leid from le where lf.prjid=le.prjid and lf.lfname=le.lfname)
where exists (select 1 from le where prjid = lf.prjid and lfname = lf.lfname and prjid = 106);

insert into tasko (prjid, taskoid, taskostat)       values (106, 'O01', 0);
insert into task (prjid, leid, taskstat, taskoid)   values (106, 'L01', 0, 'O01');
insert into task (prjid, leid, taskstat, taskoid)   values (106, 'L02', 0, 'O01');

insert into tasko (prjid, taskoid, taskostat)       values (106, 'O02', 0);
insert into task (prjid, leid, taskstat, taskoid)   values (106, 'L03', 0, 'O02');
insert into task (prjid, leid, taskstat, taskoid)   values (106, 'L04', 0, 'O02');
insert into task (prjid, leid, taskstat, taskoid)   values (106, 'L05', 0, 'O02');

COMMIT;
