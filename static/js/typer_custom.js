
    var typewriter = require('typewriter');

    var twSpan1 = document.getElementById('typewriter1');
    var twSpan2 = document.getElementById('typewriter2');
    var twSpan3 = document.getElementById('typewriter3');
    var twSpan4 = document.getElementById('typewriter4');
    var twSpan5 = document.getElementById('typewriter5');
    var twSpan6 = document.getElementById('typewriter6');
    var twSpan7 = document.getElementById('typewriter7');
    var twSpan8 = document.getElementById('typewriter8');

    var tw1 = typewriter(twSpan1).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw2 = typewriter(twSpan2).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw3 = typewriter(twSpan3).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw4 = typewriter(twSpan4).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw5 = typewriter(twSpan5).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw6 = typewriter(twSpan6).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw7 = typewriter(twSpan7).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();
    var tw8 = typewriter(twSpan8).withAccuracy(100).withMinimumSpeed(10).withMaximumSpeed(20).build();


    var msg1 = 'UNIST의';
    msg1 = Hangul.disassemble(msg1);
    msg1 = Hangul.typewrite(msg1);
    var msg2 = '모임';
    msg2 = Hangul.disassemble(msg2);
    msg2 = Hangul.typewrite(msg2);
    var msg3 = '과';
    msg3 = Hangul.disassemble(msg3);
    msg3 = Hangul.typewrite(msg3);
    var msg4 = '동아리';
    msg4 = Hangul.disassemble(msg4);
    msg4 = Hangul.typewrite(msg4);
    var msg5 = '를 위한 공간,';
    msg5 = Hangul.disassemble(msg5);
    msg5 = Hangul.typewrite(msg5);
    var msg6 = '우리는';
    msg6 = Hangul.disassemble(msg6);
    msg6 = Hangul.typewrite(msg6);
    var msg7 = '문화';
    msg7 = Hangul.disassemble(msg7);
    msg7 = Hangul.typewrite(msg7);
    var msg8 = '를 만들어갑니다.';
    msg8 = Hangul.disassemble(msg8);
    msg8 = Hangul.typewrite(msg8);

    tw1.wait(1700)
        .type(msg1)
        .type('', function() {
            tw2.type(msg2)
                .type('', function () {
                    tw3.type(msg3)
                        .type('', function () {
                            tw4.type(msg4)
                                .type('', function () {
                                    tw5.type(msg5).put('<br/>').wait(500)
                                        .type('', function () {
                                            tw6.type(msg6)
                                                .type('', function () {
                                                    tw7.type(msg7)
                                                        .type('', function () {
                                                            tw8.type(msg8)
                                                        })
                                                })
                                        })
                                })
                        })

                })
        })

