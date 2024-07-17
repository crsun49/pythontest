import uiautomator2 as u2
d = u2.connect_usb('v8eqhujjwwknkjyt')
d.app_stop("com.android.fileexplorer")
d.app_stop('com.ss.android.ugc.aweme')
d.app_start("com.android.fileexplorer")