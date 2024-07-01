SELECT ad.APNT_NO, p.PT_NAME, p.PT_NO, ad.MCDP_CD, ad.DR_NAME, ad.APNT_YMD
FROM PATIENT p join (SELECT a.APNT_NO, d.MCDP_CD, d.DR_NAME, a.APNT_YMD, a.PT_NO
                    FROM APPOINTMENT a join DOCTOR d
                    ON a.MDDR_ID = d.DR_ID
                    WHERE TO_CHAR(a.APNT_YMD, 'yyyy-MM-dd')='2022-04-13'
                     AND a.MCDP_CD = 'CS'
                     AND a.APNT_CNCL_YN = 'N') ad
ON p.PT_NO = ad.PT_NO
ORDER BY ad.APNT_YMD;
