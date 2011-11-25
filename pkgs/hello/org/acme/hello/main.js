define(["org/acme/util/logging",
	"./hello",
	"jquery"], function(logging, hello, $) {
    
    function start() {
	logging.debug("start main!");
	logging.debug(hello.hello());
	logging.debug($);
    }

    return {
	start: start
    }

});