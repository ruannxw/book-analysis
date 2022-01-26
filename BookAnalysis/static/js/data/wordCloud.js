(async () => {
    var res = await request({ url: '/v1/data/wordCloud' })
    // 实例化对象
    const wordCloud = echarts.init(document.getElementById('wordCloud'));
    let image = new Image();
    // image.src = "data:image/png;base64,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"
    image.src = '/static/images/logo.png'
    // 指定配置和数据
    let option = {
        // tooltip: {
        //     trigger: 'axis',
        //     axisPointer: {
        //         type: 'shadow'
        //     }
        // },
        grid: {
            left: '2%',
            right: '2%',
            bottom: '20%',
            top: '5%',
            containLabel: true,
            // backgroundColor: #fff
        },
        series: [
            {
                type: 'wordCloud',

                // The shape of the "cloud" to draw. Can be any polar equation represented as a
                // callback function, or a keyword present. Available presents are circle (default),
                // cardioid (apple or heart shape curve, the most known polar equation), diamond (
                // alias of square), triangle-forward, triangle, (alias of triangle-upright, pentagon, and star.

                shape: 'star',

                // Keep aspect ratio of maskImage or 1:1 for shapes
                // This option is supported from echarts-wordcloud@2.1.0
                keepAspect: false,

                // A silhouette image which the white area will be excluded from drawing texts.
                // The shape option will continue to apply as the shape of the cloud to grow.

                maskImage: image,

                // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
                // Default to be put in the center and has 75% x 80% size.

                left: 'center',
                top: 'center',
                width: '100%',
                height: '100%',
                right: null,
                bottom: null,

                // Text size range which the value in data will be mapped to.
                // Default to have minimum 12px and maximum 60px size.

                sizeRange: [12, 60],

                // Text rotation range and step in degree. Text will be rotated randomly in range [-90, 90] by rotationStep 45

                rotationRange: [-90, 90],
                rotationStep: 45,

                // size of the grid in pixels for marking the availability of the canvas
                // the larger the grid size, the bigger the gap between words.

                gridSize: 8,

                // set to true to allow word being draw partly outside of the canvas.
                // Allow word bigger than the size of the canvas to be drawn
                drawOutOfBound: false,

                // If perform layout animation.
                // NOTE disable it will lead to UI blocking when there is lots of words.
                layoutAnimation: true,

                // Global text style
                textStyle: {
                    fontFamily: 'sans-serif',
                    fontWeight: 'bold',
                    // Color can be a callback function or a color string
                    color: function () {
                        // Random color
                        return 'rgb(' + [
                            Math.round(100 + Math.random() * 155),
                            Math.round(100 + Math.random() * 155),
                            Math.round(100 + Math.random() * 155)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    focus: 'self',

                    textStyle: {
                        textShadowBlur: 10,
                        textShadowColor: '#333'
                    }
                },
                data: res
            }
        ]
    }

    image.onload = function () {
        wordCloud.setOption(option);
    };
})()


// window.addEventListener("resize", function () {
//     wordCloud.resize();
// });