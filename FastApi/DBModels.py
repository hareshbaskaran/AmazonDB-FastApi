from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .db import Base


class Buyer(Base):
    __tablename__ = "buyer"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)

    card_info = relationship("CardInfo", back_populates="buyer")
    orders = relationship("Order", back_populates="buyer")
    reviews = relationship("Review", back_populates="buyer")
    wishlist = relationship("Wishlist", uselist=False, back_populates="buyer")
    shopping_cart = relationship("ShoppingCart", uselist=False, back_populates="buyer")
    
class ContactDetails(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    address = Column(String, index=True)
    phone = Column(String, index=True)

    user = relationship("User", back_populates="contact_details")
        
class ReviewImages(Base):
    id = Column(Integer, primary_key=True, index=True)
    review_id = Column(Integer, ForeignKey("reviews.id"))
    image_url = Column(String, index=True)

    review = relationship("Review", back_populates="review_images")
    
class ProductImages(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    image_url = Column(String, index=True)

    product = relationship("Product", back_populates="product_images")
    
class ProductWishlist(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    wishlist_id = Column(Integer, ForeignKey("wishlists.id"))

    product = relationship("Product", back_populates="product_wishlist")
    wishlist = relationship("Wishlist", back_populates="product_wishlist")
    
class ProductShoppingCart(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    shopping_cart_id = Column(Integer, ForeignKey("shopping_carts.id"))

    product = relationship("Product", back_populates="product_shopping_cart")
    shopping_cart = relationship("ShoppingCart", back_populates="product_shopping_cart")
    
class ProductOrder(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))

    product = relationship("Product", back_populates="product_order")
    order = relationship("Order", back_populates="product_order")   
    
class Carrier(Base):
    __tablename__ = "carrier"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    active = Column(Boolean, default=True)
    
class Category(Base):
    __tablename__ = "category"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
class ContactDetail(Base):
    __tablename__ = "contact_detail"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    address = Column(String)
    phone = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    user = relationship("User", back_populates="contact_details")
    
class ProductImage(Base):
    __tablename__ = "product_image"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))
    
    product = relationship("Product", back_populates="product_images")
    
class ReviewImage(Base):
    __tablename__ = "review_image"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    review_id = Column(Integer, ForeignKey("review.id"))
    
    review = relationship("Review", back_populates="review_images")

class ProductWishlist(Base):
    __tablename__ = "product_wishlist"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    wishlist_id = Column(Integer, ForeignKey("wishlist.id"))
    
class ProductShoppingCart(Base):
    __tablename__ = "product_shopping_cart"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    
class ProductOrder(Base):
    __tablename__ = "product_order"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    order_id = Column(Integer, ForeignKey("order.id"))
    
class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    card_id = Column(Integer, ForeignKey("card.id"))
    address_id = Column(Integer, ForeignKey("contact_details.id"))

    buyer = relationship("Buyer", back_populates="orders")
    card = relationship("Card", back_populates="orders")
    address = relationship("ContactDetails", back_populates="orders")
    products = relationship("Product", secondary=product_order, back_populates="orders")


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    card_number = Column(String, index=True)
    card_holder_name = Column(String)
    expiration_date = Column(String)
    cvv = Column(String)

    buyer = relationship("Buyer", back_populates="cards")
    orders = relationship("Order", back_populates="card")


class ContactDetails(Base):
    __tablename__ = "contact_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    address = Column(Text)
    phone_number = Column(String)

    user = relationship("User", back_populates="contact_details")
    orders = relationship("Order", back_populates="address")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    product_id = Column(Integer, ForeignKey("product.id"))

    buyer = relationship("Buyer", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")
    review_images = relationship("ReviewImage", back_populates="review")


class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("buyer.id"))

    buyer = relationship("Buyer", back_populates="wishlist")
    products = relationship("Product", secondary=product_wishlist, back_populates="wishlists")


class ProductImage(Base):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    product_id = Column(Integer, ForeignKey("product.id"))

    product = relationship("Product", back_populates="product_images")


class ReviewImage(Base):
    __tablename__ = "review_image"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    review_id = Column(Integer, ForeignKey("review.id"))

    review = relationship("Review", back_populates="review_images")


class Carrier(Base):
    __tablename__ = "carrier"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship("Product", back_populates="carrier")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship("Product", back_populates="category")
