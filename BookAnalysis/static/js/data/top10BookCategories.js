(async () => {
    var res = await request({ url: '/v1/data/top10BookCategories' })
    // 实例化对象
    const top10BookCategories = echarts.init(document.getElementById('top10BookCategories'));

    top10BookCategories.setOption({
        grid: {
            left: '3%',
            right: '2%',
            bottom: '2%',
            top: '15%',
            containLabel: true,
            // backgroundColor: #fff
        },
        xAxis: {
            data: res['xAxis'],
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10,
            name: '图书分类',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                // padding: [5, 0, 0, -5]
            },
            nameGap: 25, // 坐标轴名称与轴线之间的距离
            axisLabel: {
                // 坐标轴标签
                show: true, // 是否显示
                inside: false, // 是否朝内
                // rotate: 45, // 旋转角度
                // margin: 15, // 刻度标签与轴线之间的距离
                color: '#fff', // 默认取轴线的颜色
                textStyle: {
                    color: '#fff'
                }
            }
        },
        yAxis: {
            name: '数量 单位: 万（本）',
            type: 'value',
            nameTextStyle: {
                // 坐标轴名称样式
                color: '#fff',
                padding: [0, 0, 0, 50] // 坐标轴名称相对位置
            },
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                textStyle: {
                    color: '#fff'
                },
                formatter: function (value) {
                    if (value > 10000) {
                        return value / 10000 + 'w'
                    } else if (value > 1000) {
                        return value / 1000 + 'k'
                    } else {
                        return value
                    }
                }
            }
        },
        dataZoom: [
            {
                type: 'inside'
            }
        ],
        series: [
            {
                name: '图书数量',
                type: 'bar',
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1, color: '#188df0' }
                    ])
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2378f7' },
                            { offset: 0.7, color: '#2378f7' },
                            { offset: 1, color: '#83bff6' }
                        ])
                    }
                },
                data: res['yAxis']
            }
        ],
        tooltip: {
            trigger: 'axis', //坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用
            axisPointer: {
                // 坐标轴指示器，坐标轴触发有效
                type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
            }
        }
    });
})()
// 指定配置和数据


// window.addEventListener("resize", function () {
//     top10BookCategories.resize();
// });