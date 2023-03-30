from typing import List,Optional

from pydantic import BaseModel


class BuyerBase(BaseModel):
    pass


class BuyerCreate(BuyerBase):
    pass


class Buyer(BuyerBase):
    user_id: int

    class Config:
        orm_mode = True


class UserBuyers(BaseModel):
    buyers: List[Buyer] = []

# user table
class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_seller: bool
    is_active: bool
    address: Optional[List["Address"]] = []

    class Config:
        orm_mode = True

# address table
class AddressBase(BaseModel):
    address_line_1: str
    address_line_2: Optional[str] = ""
    city: str
    state: str
    country: str
    zip_code: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# phone table
class PhoneBase(BaseModel):
    phone_number: str

class PhoneCreate(PhoneBase):
    pass

class Phone(PhoneBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# card_info table
class CardInfoBase(BaseModel):
    card_number: str
    cardholder_name: str
    expiry_date: str
    cvv: str

class CardInfoCreate(CardInfoBase):
    pass

class CardInfo(CardInfoBase):
    id: int
    buyer_id: int

    class Config:
        orm_mode = True

# product table
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    quantity: int
    seller_id: int
    carrier_id: int
    category_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    reviews: Optional[List["Review"]] = []
    product_images: Optional[List["ProductImage"]] = []

    class Config:
        orm_mode = True

# category table
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: Optional[List[Product]] = []

    class Config:
        orm_mode = True

# carrier table
class CarrierBase(BaseModel):
    name: str

class CarrierCreate(CarrierBase):
    pass

class Carrier(CarrierBase):
    id: int
    products: Optional[List[Product]] = []

    class Config:
        orm_mode = True

# order table
class OrderBase(BaseModel):
    total_price: float
    buyer_id: int
    card_id: Optional[int] = None
    address_id: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    products: Optional[List[Product]] = []

    class Config:
        orm_mode = True

# review table
class ReviewBase(BaseModel):
    title: str
    description: str
    rating: int
    product_id: int
    buyer_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    review_images: Optional[List["ReviewImage"]] = []

    class Config:
        orm_mode = True

# wishlist table
class WishlistBase(BaseModel):
    name: str
    buyer_id: int

class WishlistCreate(WishlistBase):
    pass

class Wishlist(WishlistBase):
    id: int
    products: Optional[List[Product]] = []

    class Config:
        orm_mode = True
        
#shopping cart

class ShoppingCartBase(BaseModel):
    buyer_id: int

class ShoppingCartCreate(ShoppingCartBase):
    pass

class ShoppingCartUpdate(ShoppingCartBase):
    pass

class ShoppingCart(ShoppingCartBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True        


