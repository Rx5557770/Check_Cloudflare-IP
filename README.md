介紹：

通過指定的IP文件檢查是否爲反代Cloudflare的IP

環境：python(需要安裝requests庫)

脚本自動識別當前目錄下的 IPS.txt 文件，若不存在則手動輸入文件夾路徑，注意：路徑後面需要加 /

獲取cloudflare的反代IP，保存到 Success_IPS.txt 中

獲取失敗的IP，保存到 Fail_IPS.txt 中

探測失敗的IP，保存到 Continue_IPS.txt 中

