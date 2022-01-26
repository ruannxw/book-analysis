const Colors = [
    '#c23531',
    '#2f4554',
    '#61a0a8',
    '#d48265',
    '#91c7ae',
    '#749f83',
    '#ca8622',
    '#bda29a',
    '#6e7074',
    '#546570',
    '#c4ccd3'
];

(async () => {
    var xAxis = []
    var yAxis = []
    var year;
    // const data = [];
    // for (let i = 0; i < 5; ++i) {
    //     data.push(Math.round(Math.random() * 200));
    // }
    const data = await request({ url: '/v1/data/dynamicNumberOfPublisher' })
    const dynamicNumberOfPublisher = echarts.init(document.getElementById('dynamicNumberOfPublisher'), 'dark');
    dynamicNumberOfPublisher.setOption({
        backgroundColor: 'transparent',
        grid: {
            left: '3%',
            right: '15%',
            bottom: '2%',
            top: '5%',
            containLabel: true,
            // backgroundColor: #fff
        },
        xAxis: {
            // max: 'dataMax'
        },
        yAxis: {
            type: 'category',
            // data: xAxis,
            inverse: true,
            animationDuration: 300,
            animationDurationUpdate: 600,
            max: 9, // only the largest 3 bars will be displayed
            axisLabel: {
                // 坐标轴标签
                show: true, // 是否显示
                formatter: function (value) {
                    return value.length > 2 ? value.substring(0, 2) + '...' : value
                }
            }
        },
        tooltip: {
            trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
            }
        },
        series: [
            {
                realtimeSort: true,
                name: '出版数量',
                type: 'bar',
                // data: yAxis,
                label: {
                    show: true,
                    position: 'right',
                    valueAnimation: true
                },
                itemStyle: {
                    color: function (param) {
                        // console.log(param)
                        return Colors[param.dataIndex % Colors.length];
                    }
                },
            }
        ],
        // legend: {
        //     show: true
        // },
        animationDuration: 0,
        animationDurationUpdate: 3000,
        animationEasing: 'linear',
        animationEasingUpdate: 'linear',
        graphic: {
            elements: [
                {
                    type: 'text',
                    right: 20,
                    bottom: 40,
                    style: {
                        text: year,
                        font: 'bolder 30px monospace',
                        fill: 'rgba(100, 100, 100)'
                    },
                    z: 100
                }
            ]
        }
    })
    for (const year in data['data']) {
        dynamicNumberOfPublisher.setOption({
            yAxis: {
                data: data['data'][year]['xAxis'],
            },
            series: [
                {
                    name: `${year}年出版数量`,
                    type: 'bar',
                    data: data['data'][year]['yAxis'],
                }
            ],
            graphic: {
                elements: [
                    {
                        type: 'text',
                        right: 20,
                        bottom: 40,
                        style: {
                            text: year,
                            font: 'bolder 30px monospace',
                            fill: 'rgba(100, 100, 100)'
                        },
                        z: 100
                    }
                ]
            }
        });
        await sleep(1200)
        // sleep_time += Math.round(Math.random() * 200)
    }
})()



