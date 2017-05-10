function _string(a)
{
	var r = "0000"+a.toString(4);
	r = r.substr(r.length-4,4);
	return r;
}

function _chinzo_encode(c)
{
	for (i=0; i<aa.length; i++) {
		c = c.split(aa[i][0]).join(aa[i][1]);
	}

	return c;
}

function _chinzo_decode(c, s)
{
	for(i=0; i<aa.length; i++) {
		c = c.split(aa[i][1]).join(aa[i][0]);
	}

	return c;
}

function _encode(a)
{
	if (a=='') {
		return a;
	}

	u = a.match(/吴/);

	if (u) {
		return a;
	}

	a = a.split('oo').join('讲');
	a = a.split('ii').join('邻');
	a = a.split('ee').join('头');
	a = a.split('tt').join('会');
	a = a.split('rr').join('歷');
	a = encodeURIComponent(a);
	r ='';

	for(i=0; i<a.length; i++) {
		d = _string(a.charCodeAt(i));
		//r+=d+' ';// caso que queira espaco entre os caracteres
		r+=d;
	}

	//return r;

	r = _chinzo_encode(r);
	return r+'吴';
}

function _decode(a)
{
	if (a=='') {
		return'';
	}

	r = '';
	a = a.split('吴').join('');
	a = a.replace(/\s+/ig,' ');
	a = a.split(' ').join('');
	a = _chinzo_decode(a);

	for(i=0; i<a.length; i+=4) {
		r+=String.fromCharCode(parseInt(a.substr(i,4),4));
	}

	r = decodeURIComponent(r);
	r = r.split('讲').join('oo');
	r = r.split('邻').join('ii');
	r = r.split('头').join('ee');
	r = r.split('会').join('tt');
	r = r.split('歷').join('rr');
	return r;
}