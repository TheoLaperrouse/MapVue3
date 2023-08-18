export const getReviews = async () => {
    try {
        const response = await fetch('http://127.0.0.1:5000/reviews');
        if (!response.ok) {
            throw new Error('Erreur lors de la récupération des marqueurs');
        }
        const reviews = await response.json();
        return reviews;
    } catch (error) {
        console.error('Erreur:', error);
    }
};

export const postReview = async (review) => {
    try {
        return fetch('http://localhost:5000/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(review),
        });
    } catch (error) {
        console.error('Erreur:', error);
    }
};
