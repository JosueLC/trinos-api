//interface trino
export interface trino {
    id: string;
    content: string;
    created_at:Date;
    updated_at:Date;
    by: {
        id: string;
        username: string;
        email: string;
    };
}