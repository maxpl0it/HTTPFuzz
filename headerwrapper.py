from headers import *

class HeaderWrapper:
	def get_headers(self):
		return [accept.Accept, acceptcharset.AcceptCharset, acceptencoding.AcceptEncoding, acceptlanguage.AcceptLanguage, acceptdatetime.AcceptDatetime, accesscontrolrequestmethod.AccessControlRequestMethod, accesscontrolrequestheaders.AccessControlRequestHeaders, authorization.Authorization, cachecontrol.CacheControl, connection.Connection, contentlength.ContentLength, contentmd5.ContentMD5, contenttype.ContentType, cookie.Cookie, date.Date, expect.Expect, forwarded.Forwarded, email.Email, host.Host, ifmatch.IfMatch, ifmodifiedsince.IfModifiedSince, ifnonematch.IfNoneMatch, ifrange.IfRange, ifunmodifiedsince.IfUnmodifiedSince, maxforwards.MaxForwards, origin.Origin, pragma.Pragma, proxyauthorization.ProxyAuthorization, range.Range, referer.Referer, te.TE, useragent.UserAgent, upgrade.Upgrade, via.Via, warning.Warning]
