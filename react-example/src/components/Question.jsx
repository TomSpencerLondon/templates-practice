function Question(props) {
    return (
        <>
           <h2>{props.item.text}</h2>
           <ul>
            {props.item.choices.map((value, index) => 
                (<li key={index}>{value}</li>)
            )}
           </ul>
           <h3>{props.item.answer}</h3>
           <div id="line"></div>
        </>
    )
}

export default Question;
