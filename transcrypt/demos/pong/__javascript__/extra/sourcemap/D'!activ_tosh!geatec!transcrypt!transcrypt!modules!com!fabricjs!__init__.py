fabric = __pragma__ ('js',
	'''
(function () {{
	var exports = {{}};
	{}	// Puts fabric in exports and in global window
	delete window.fabric;
	return exports;
}}) () .fabric;
	''',
	__include__ ('com/fabricjs/__javascript__/fabric.js')
)
