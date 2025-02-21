const mera = async ()=>{
    const url = 'http://localhost:8900/'
    const options = {
        method: "GET",
    }
    await fetch(url, options);
}

export const Something = ()=>{
    return <button onClick={mera}> mybtn</button>
}