<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Factories\HasFactory;
class Quest extends Model
{
    use HasFactory;

    protected $fillable = ['title', 'category_id', 'description', 'reward'];

    public function category(){
        return $this->belongsTo(Category::class);
    }
}
