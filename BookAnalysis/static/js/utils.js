const request = (params) => {
    const baseUrl = ''
    return new Promise((resolve, reject) => {
        $.ajax({
            ...params,
            success: (result) => {
                resolve(result.data)
            },
            fail: (err) => {
                reject(err)
            }
        });
    })
}

// async function getData() {
//     const res = await request({url: '/data'})
// }
