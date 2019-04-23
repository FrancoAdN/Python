
class Rect:
    def __init__ (self, obj, surf, background, color, pos, r, rs):
        self.rot = r
        self.rot_speed = rs
        self.image_org = obj.Surface(surf)
        self.image_org.set_colorkey(background)
        self.image_org.fill(color)

        self.image = image_org.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (pos[0], pos[1])

    def show(self, obj, screen):
        self.old_center = self.rect.center   
        self.rot = (self.rot + self.rot_speed) % 360  
        # rotating the orignal image  
        self.new_image = obj.transform.rotate(self.image_orig , self.rot)  
        self.rect = self.new_image.get_rect()  
        # set the rotated rectangle to the old center  
        self.rect.center = self.old_center  
        # drawing the rotated rectangle to the screen  
        screen.blit(self.new_image , self.rect)  
        # flipping the display after drawing everything  
        obj.display.flip()  
